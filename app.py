import pymongo
from flask import Flask, render_template, request
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://arihant:7ELd5M1DQtCYO2Ks@cluster0.omldzri.mongodb.net/?retryWrites=true&w"
                             "=majority", server_api=ServerApi('1'))

db = client.get_database('project')
col = db.get_collection('suicide')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def worldwide():
    data = col.aggregate([{"$group": {"_id": "$year", "sui_no": {"$sum": "$suicides_no"}}}, {"$sort": {"_id": 1}}])
    res1 = []
    for d in data:
        res1.append(list(d.values()))

    data = col.aggregate([{"$group": {"_id": "$age", "sui_no": {"$sum": "$suicides_no"}}}, {"$sort": {"_id": 1}}])
    res2 = [["Age", "Suicides"]]
    for d in data:
        res2.append(list(d.values()))
    temp = res2.pop(4)
    res2.insert(1, temp)

    data = col.aggregate([{"$group": {"_id": "$sex", "sui_no": {"$sum": "$suicides_no"}}}])
    res3 = [["Gender", "Suicides"]]
    for d in data:
        res3.append(list(d.values()))
    return render_template('worldwide.html', year_data=res1[:-1], age_data=res2, gender_data=res3)


@app.route('/country', methods=['GET', 'POST'])
def country():
    data = col.aggregate([{"$group": {"_id": "$country", "sui_no": {"$sum": "$suicides_no"}}}, {"$sort": {"_id": 1}}])
    res1 = [['Country', 'Suicides']]
    for d in data:
        res1.append(list(d.values()))

    data = col.aggregate(
        [{"$group": {"_id": {"country": "$country", "gender": "$sex"}, "sui_no": {"$sum": "$suicides_no"}}},
         {"$sort": {"_id.country": 1}}])
    res2 = [['Gender', 'Male', 'Female']]
    m = {}
    idx = {'male': 1, 'female': 2}
    for d in data:
        l = list(d.values())
        if l[1] == 0:
            continue
        ctn = l[0]['country']
        if ctn not in m:
            m[l[0]['country']] = [ctn, 0, 0]
        m[l[0]['country']][idx[l[0]['gender']]] = l[1]

    data = col.aggregate(
        [{"$group": {"_id": {"country": "$country", "age": "$age"}, "sui_no": {"$sum": "$suicides_no"}}},
         {"$sort": {"_id.country": 1}}])
    res3 = [['Age', '5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']]
    mp = {}
    idx = {'5-14 years': 1, '15-24 years': 2, '25-34 years': 3, '35-54 years': 4, '55-74 years': 5, '75+ years': 6}
    for d in data:
        l = list(d.values())
        if l[1] == 0:
            continue
        ctn = l[0]['country']
        if ctn not in mp:
            mp[l[0]['country']] = [ctn, 0, 0, 0, 0, 0, 0]
        mp[l[0]['country']][idx[l[0]['age']]] = l[1]
    return render_template('country.html', country_data=res1, gender_data=res2+list(m.values()),
                           age_data=res3+list(mp.values()))


@app.route('/modify', methods=['GET'])
def modify(it=False, ut=False, dt=False):
    countries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire,'
                ' Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil',
                 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi',
                 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad',
                 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
                 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia',
                 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
                 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
                 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
                 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
                 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
                 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands',
                 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia',
                 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
                 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of",
                 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon',
                 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia,'
                ' Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
                 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of',
                 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique',
                 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua',
                 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan',
                 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
                 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania',
                 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha',
                 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon',
                 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
                 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)',
                 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
                 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
                 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste',
                 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
                 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.',
                 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
    age_groups = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']
    return render_template('modify.html', countries=countries, age_groups=age_groups, insert=it, update=ut, delete=dt)


@app.route('/insert', methods=['POST'])
def insert():
    col.insert_one({'country': request.form.get('country'), 'year': int(request.form.get('year')),
                    'age': request.form.get('age'), 'sex': request.form.get('gender'),
                    'population': int(request.form.get('population')), 'suicides_no': int(request.form.get('suicides'))})
    return modify(it=True)


@app.route('/delete', methods=['POST'])
def delete():
    col.delete_one({'country': request.form.get('country'), 'year': int(request.form.get('year')),
                    'age': request.form.get('age'), 'sex': request.form.get('gender')})
    return modify(dt=True)


@app.route('/update', methods=['POST'])
def update():
    col.update_one({'country': request.form.get('country'), 'year': int(request.form.get('year')),
                    'age': request.form.get('age'), 'sex': request.form.get('gender')},
                   {'$set': {'population': int(request.form.get('population')),
                'suicides_no': int(request.form.get('suicides'))}})
    return modify(ut=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
