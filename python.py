from requests import Session

s = Session()
access_token ='EAAGNO4a7r2wBOwAwWiTAFmdNUjcPmVZADv9tLDqkFMRkWPRj5MVwv1rEzO75w0rL9gzfocCGyaeLY5PzjxV3p1R66OexAmUAD3nfXFJRhY6iGnuIz1zAjBICXT3pjZBLduz39iU0jblCNquwv1X12q5ZAcO0EvR7CPGqfavjS5j3ZABHZAU1yYIyzjwZDZD'
pageId = 'beegamingAOV'
demo = 0 
data = s.get('https://graph.facebook.com/v20.0/vietalents?access_token=EAAGNO4a7r2wBOwAwWiTAFmdNUjcPmVZADv9tLDqkFMRkWPRj5MVwv1rEzO75w0rL9gzfocCGyaeLY5PzjxV3p1R66OexAmUAD3nfXFJRhY6iGnuIz1zAjBICXT3pjZBLduz39iU0jblCNquwv1X12q5ZAcO0EvR7CPGqfavjS5j3ZABHZAU1yYIyzjwZDZD&debug=all&format=json&method=get&origin_graph_explorer=1&pretty=0&suppress_http_code=1&transport=cors')
print(data.json())
# for x in data.json()["videos"]["data"]:
#     demo += 1
#     if 'source' in x :
#         video_url = x['source']
#         print(video_url) 
