d3.select('#step').graphviz().scale(2.3).height(document.getElementById('step').clientHeight).width(800*1.9).renderDot(`digraph pasos {
    rankdir = TB;
    node0 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Estado Inicial</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="white" width="100" height="30">Li</td>
    <td BGCOLOR="white" width="100" height="30">He</td>
    <td BGCOLOR="white" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="white" width="100" height="30">C</td>
    <td BGCOLOR="white" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node0 -> node1[style=invis];
    node1 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 1</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="white" width="100" height="30">He</td>
    <td BGCOLOR="white" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="white" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node1 -> node2[style=invis];
    node2 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 2</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="white" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node2 -> node3[style=invis];
    node3 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 3</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">Be</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node3 -> node4[style=invis];
    node4 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 4</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">Be</td>
    <td BGCOLOR="gray" width="100" height="30" border="3">H</td>
    </tr>
    </TABLE>>
    ];
    node4 -> node5[style=invis];
    node5 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 5</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">Be</td>
    <td BGCOLOR="gray" width="100" height="30" border="3">H</td>
    </tr>
    </TABLE>>
    ];
    node5 -> node6[style=invis];
    node6 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 6</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node6 -> node7[style=invis];
    node7 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 7</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="gray" width="100" height="30" border="3">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node7 -> node8[style=invis];
    node8 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 8</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="gray" width="100" height="30" border="3">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="white" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node8 -> node9[style=invis];
    node9 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 9</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">He</td>
    <td BGCOLOR="white" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="gray" width="100" height="30" border="3">C</td>
    <td BGCOLOR="white" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node9 -> node10[style=invis];
    node10 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 10</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#B9E0FF" width="100" height="30">Li</td>
    <td BGCOLOR="white" width="100" height="30">He</td>
    <td BGCOLOR="white" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="white" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    node10 -> node11[style=invis];
    node11 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td border="0" colspan="4" align="left">Segundo 11</td>
    </tr><tr>
    <td BGCOLOR="#B9E0FF" width="60" height="30">Pin 1</td>
    <td BGCOLOR="gray" width="100" height="30" border="3">Li</td>
    <td BGCOLOR="white" width="100" height="30">He</td>
    <td BGCOLOR="white" width="100" height="30">N</td>
    </tr>
    <tr>
    <td BGCOLOR="#8D9EFF" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#8D9EFF" width="100" height="30">C</td>
    <td BGCOLOR="white" width="100" height="30">Be</td>
    <td BGCOLOR="white" width="100" height="30">H</td>
    </tr>
    </TABLE>>
    ];
    }`)