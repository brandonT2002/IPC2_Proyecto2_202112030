dot = d3.select('#machine').graphviz().scale(2.3).height(document.getElementById('machine').clientHeight).width(800*1.9).renderDot(`digraph maquina {
    node1 [shape=none, margin=0, label=
    <<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="5">
    <tr>
    <td BGCOLOR="gray" width="60" height="30">Pin 1</td>
    <td BGCOLOR="#EAE37B" width="100" height="30">3<br align="left"/>Li<br/>Litio</td>
    <td BGCOLOR="#F675BA" width="100" height="30">2<br align="left"/>He<br/>Helio</td>
    <td BGCOLOR="#8F38CC" width="100" height="30">7<br align="left"/>N<br/>Nitrógeno</td>
    </tr>
    <tr>
    <td BGCOLOR="gray" width="60" height="30">Pin 2</td>
    <td BGCOLOR="#98ABA3" width="100" height="30">6<br align="left"/>C<br/>Carbono</td>
    <td BGCOLOR="#295F82" width="100" height="30">4<br align="left"/>Be<br/>Berilio</td>
    <td BGCOLOR="#40A90F" width="100" height="30">1<br align="left"/>H<br/>Hidrógeno</td>
    </tr>
    </TABLE>>
    ];
    }`)