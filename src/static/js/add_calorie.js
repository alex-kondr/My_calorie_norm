const form = document.forms[0]


form.addEventListener('submit', async event => {
    event.preventDefault() 
    body1 = JSON.stringify({
                    'date': form.date.value,
                    'height': form.height.value,
                    'weight': form.weight.value,
                    'age': form.age.value
                })

    const response = await fetch(
        `/add_calorie`,
            {
                method: 'POST',
                body: body1
            }
    )

    result = await response.json()
    console.log("response status", response.status)
    console.log("result: ", result)
    console.log("body1: ", body1)

    // if (response.status === 201) {

    //     form.hidden = true
    //     detail.innerHTML = result.detail
    //     buttons.hidden = false
    // }
    // else {
    //     form.hidden = true
    //     buttons.hidden = false
    //     msg = ""
    //     for (res of result.detail) {
    //         msg = msg + res.loc[1] + "-error: " + res.msg + "\n"
    //     }
    //     detail.innerHTML = msg + "\n" + result.detail
    // }
})


