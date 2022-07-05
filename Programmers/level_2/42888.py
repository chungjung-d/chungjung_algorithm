#오픈채팅방

def solution(record):

    # Enter = 0 / Leave  = 1
    id_name_dict = {}
    id_state = []

    answer = []

    for i in record:
        i_list = i.split(' ')

        state = i_list[0]
        id = i_list[1]
        if len(i_list) == 3:
            name = i_list[2]
            id_name_dict[id] = name

        if(state == 'Enter'):
            id_state.append([0,id])

        if(state == 'Leave'):
            id_state.append([1,id])

    for k in id_state:
        temp_name = id_name_dict[k[1]]+'님이 '
        temp_state = '들어왔습니다.' if k[0] == 0 else '나갔습니다.'
        answer.append(temp_name+temp_state)

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])