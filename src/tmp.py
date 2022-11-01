# from const import OrderStatus
#
# if __name__ == '__main__':
#     print(OrderStatus.get_key())

# a = {1: 1, 2: 2, 3: 3, 4: 4}
# a = ['1', '2', '3', '4', '5']
#
# from datetime import datetime
#
# now = datetime.now()
# a = now.strftime('%F %X,%f')[:-3]
#
# results = ['abc']
# test = ['1111111']
# test2 = ['2222222']
# results.extend([test, test2])
# # results.append({test, test2})  #會黏再一起
# print(results)
#
# class Myteam11:
#     class Sport:
#         CRICKET = 1
#         SOCCER = 2
#         KABADDI = 3
#         BASKETBALL = 5
#         BASEBALL = 8
#
# class UpdateMatch:
#     _SPORTS = {
#         Myteam11.Sport.CRICKET,
#         Myteam11.Sport.SOCCER,
#         Myteam11.Sport.BASKETBALL,
#         Myteam11.Sport.KABADDI,
#     }
#
#     @classmethod
#     def test(cls):
#         for i in cls._SPORTS:
#             return i
#
#
# if __name__ == '__main__':
#     print(UpdateMatch._SPORTS)
#     print(UpdateMatch.test())


from redis import StrictRedis

db = StrictRedis(host='localhost', port=6379, db=0)
# db.set('vicky', '1234567890')
# output = db.get('vicky')


# rs = redis.Redis(host='localhost')
# rs.set('Vicky', 'POCKY')
# output = rs.get('Vicky')
# print(output)
# print(type(output))
