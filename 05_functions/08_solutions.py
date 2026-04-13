def sol(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

sol(name='ironman', power='infinity stone')
sol(name='captain')
sol(name='enemy', power='infinity stone', enemy='thanos', ally='spiderman')