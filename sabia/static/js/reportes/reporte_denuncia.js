var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');
var date_primera = '2022-01-01';
function generate_report(){
var parameters = {
     'action':'searchdata',
     'start_date':'2022-01-29',
     'end_date':'2022-09-26',
     };
     if(date_range !== null){

     parameters['start_date']= date_range.startDate.format('YYYY-MM-DD');
     parameters['end_date']= date_range.endDate.format('YYYY-MM-DD');
     }
$(function () {
    $('#producto').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
         /*   url: 'window.location.pathname',*/
            type: 'POST',
            data: parameters,
            dataSrc: ""
        },
      /*  order:false,
        info:false,*/
        ordering:false,
  /*      paging:false,
        searching:false,*/
        dom:'Bfrtip',

buttons: [
            {
                extend: 'excelHtml5',
                text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
                titleAttr: 'Excel',
                className: 'btn btn-success btn-flat btn-xs'
            },
            {
                extend: 'pdfHtml5',
                text: 'Descargar Pdf <i class="fas fa-file-pdf"></i>',
                titleAttr: 'PDF',
                className: 'btn btn-danger btn-flat btn-xs',
                orientation: 'landscape',
                pageSize: 'LEGAL',
             /*   customize: function (doc) {
                    doc.styles = {
                        header: {
                            fontSize: 18,
                            bold: true,
                            alignment: 'center'
                        },
                        subheader: {
                            fontSize: 13,
                            bold: true
                        },
                        quote: {
                            italics: true
                        },
                        small: {
                            fontSize: 8
                        },
                        tableHeader: {
                            bold: true,
                            fontSize: 11,
                            color: 'white',
                            fillColor: '#2d4154',
                            alignment: 'center'
                        }
                    };
                    doc.content[1].table.widths = ['20%','20%','15%','15%','15%','15%'];
                    doc.content[1].margin = [0, 35, 0, 0];
                    doc.content[1].layout = {};
                    doc['footer'] = (function (page, pages) {
                        return {
                            columns: [
                                {
                                    alignment: 'left',
                                    text: ['Fecha de creación: ', {text: date_now}]
                                },
                                {
                                    alignment: 'right',
                                    text: ['página ', {text: page.toString()}, ' de ', {text: pages.toString()}]
                                }
                            ],
                            margin: 20
                        }
                    });

                }*/
            }
        ],
        columnDefs: [
            {
                targets: [''],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {

                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
}

$(function(){

   $('input[name="date_range"]').daterangepicker( {
       locale:{
        format:'YYYY-MM-DD',
    }
    }).on('apply.daterangepicker', function(ev, picker){
    date_range =picker;
    generate_report();
    }).on('cancel.daterangepicker', function(ev, picker) {
        $(this).data('daterangepicker').setStartDate(date_primera);
        $(this).data('daterangepicker').setEndDate(date_now);
        date_range=picker;
         generate_report();
    });
generate_report();
});