# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSTStylePropertyArchiving.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import numbers_parser.generated.TSPMessages_pb2 as TSPMessages__pb2
import numbers_parser.generated.TSDArchives_pb2 as TSDArchives__pb2
import numbers_parser.generated.TSKArchives_pb2 as TSKArchives__pb2
import numbers_parser.generated.TSSArchives_pb2 as TSSArchives__pb2
import numbers_parser.generated.TSWPArchives_pb2 as TSWPArchives__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fTSTStylePropertyArchiving.proto\x12\x03TST\x1a\x11TSPMessages.proto\x1a\x11TSDArchives.proto\x1a\x11TSKArchives.proto\x1a\x11TSSArchives.proto\x1a\x12TSWPArchives.proto\"\x83\x01\n\x1d\x44\x65precated_TableStrokeArchive\x12\"\n\x06stroke\x18\x01 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x16\n\nbackground\x18\x02 \x01(\x08\x42\x02\x18\x01\x12\x13\n\x07opacity\x18\x03 \x01(\x02\x42\x02\x18\x01\x12\x11\n\x05\x65mpty\x18\x04 \x01(\x08\x42\x02\x18\x01\"\xcf\x04\n\x1a\x43\x65llStylePropertiesArchive\x12#\n\tcell_fill\x18\x01 \x01(\x0b\x32\x10.TSD.FillArchive\x12\x11\n\ttext_wrap\x18\x03 \x01(\x08\x12\x41\n\x15\x64\x65precated_top_stroke\x18\x04 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x43\n\x17\x64\x65precated_right_stroke\x18\x05 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x44\n\x18\x64\x65precated_bottom_stroke\x18\x06 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x42\n\x16\x64\x65precated_left_stroke\x18\x07 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x1a\n\x12vertical_alignment\x18\x08 \x01(\x05\x12%\n\x07padding\x18\t \x01(\x0b\x32\x14.TSWP.PaddingArchive\x12&\n\ntop_stroke\x18\n \x01(\x0b\x32\x12.TSD.StrokeArchive\x12(\n\x0cright_stroke\x18\x0b \x01(\x0b\x32\x12.TSD.StrokeArchive\x12)\n\rbottom_stroke\x18\x0c \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\'\n\x0bleft_stroke\x18\r \x01(\x0b\x32\x12.TSD.StrokeArchive\"\x9f\x02\n\"Deprecated_StrokePresetDataArchive\x12H\n\x1c\x64\x65precated_horizontal_stroke\x18\x02 \x02(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x46\n\x1a\x64\x65precated_vertical_stroke\x18\x01 \x02(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x46\n\x1a\x64\x65precated_exterior_stroke\x18\x03 \x02(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x1f\n\x17\x64\x65precated_visible_mask\x18\x05 \x02(\x05\"\xb8\x01\n\x17StrokePresetDataArchive\x12-\n\x11horizontal_stroke\x18\x01 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12+\n\x0fvertical_stroke\x18\x02 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12+\n\x0f\x65xterior_stroke\x18\x03 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x14\n\x0cvisible_mask\x18\x04 \x01(\x05\"\x9a\x01\n\x17StrokePresetListArchive\x12\r\n\x05\x63ount\x18\x01 \x02(\x05\x12\x42\n\x11\x64\x65precated_preset\x18\x02 \x03(\x0b\x32\'.TST.Deprecated_StrokePresetDataArchive\x12,\n\x06preset\x18\x03 \x03(\x0b\x32\x1c.TST.StrokePresetDataArchive\"\xb0&\n\x1bTableStylePropertiesArchive\x12\x13\n\x0b\x62\x61nded_rows\x18\x01 \x01(\x08\x12%\n\x0b\x62\x61nded_fill\x18\x02 \x01(\x0b\x32\x10.TSD.FillArchive\x12 \n\x18\x62\x65haves_like_spreadsheet\x18\x15 \x01(\x08\x12\x13\n\x0b\x61uto_resize\x18\x16 \x01(\x08\x12R\n&deprecated_header_row_separator_stroke\x18\x04 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12O\n#deprecated_header_row_border_stroke\x18\x05 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12S\n\'deprecated_header_row_horizontal_stroke\x18\x17 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12Q\n%deprecated_header_row_vertical_stroke\x18\x18 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12R\n&deprecated_header_column_border_stroke\x18\x07 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12U\n)deprecated_header_column_separator_stroke\x18\x08 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12V\n*deprecated_header_column_horizontal_stroke\x18\x19 \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12T\n(deprecated_header_column_vertical_stroke\x18\x1a \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12R\n&deprecated_footer_row_separator_stroke\x18\n \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12O\n#deprecated_footer_row_border_stroke\x18\x0b \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12S\n\'deprecated_footer_row_horizontal_stroke\x18\x1b \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12Q\n%deprecated_footer_row_vertical_stroke\x18\x1c \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12Z\n.deprecated_table_body_horizontal_border_stroke\x18\x0c \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12X\n,deprecated_table_body_vertical_border_stroke\x18\x1d \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12S\n\'deprecated_table_body_horizontal_stroke\x18\x1e \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12Q\n%deprecated_table_body_vertical_stroke\x18\x1f \x01(\x0b\x32\".TST.Deprecated_TableStrokeArchive\x12\x38\n\x12stroke_preset_list\x18  \x01(\x0b\x32\x1c.TST.StrokePresetListArchive\x12\x19\n\x11v_strokes_visible\x18! \x01(\x08\x12\x19\n\x11h_strokes_visible\x18\" \x01(\x08\x12\x1c\n\x14hr_separator_visible\x18# \x01(\x08\x12\x1c\n\x14hc_separator_visible\x18$ \x01(\x08\x12 \n\x18\x66ooter_separator_visible\x18% \x01(\x08\x12\x1c\n\x14table_border_visible\x18& \x01(\x08\x12#\n\x1btable_header_border_visible\x18\' \x01(\x08\x12 \n\x18table_hc_divider_visible\x18* \x01(\x08\x12 \n\x18table_hr_divider_visible\x18+ \x01(\x08\x12$\n\x1ctable_footer_divider_visible\x18, \x01(\x08\x12!\n\x19OBSOLETE_master_font_size\x18( \x01(\x05\x12\x1a\n\x12master_font_family\x18) \x01(\t\x12\x35\n\x11writing_direction\x18- \x01(\x0e\x32\x1a.TSWP.WritingDirectionType\x12\x37\n\x1bheader_row_separator_stroke\x18. \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x34\n\x18header_row_border_stroke\x18/ \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x38\n\x1cheader_row_horizontal_stroke\x18\x30 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1aheader_row_vertical_stroke\x18\x31 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x37\n\x1bheader_column_border_stroke\x18\x32 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12:\n\x1eheader_column_separator_stroke\x18\x33 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12;\n\x1fheader_column_horizontal_stroke\x18\x34 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1dheader_column_vertical_stroke\x18\x35 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x37\n\x1b\x66ooter_row_separator_stroke\x18\x36 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x34\n\x18\x66ooter_row_border_stroke\x18\x37 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x38\n\x1c\x66ooter_row_horizontal_stroke\x18\x38 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1a\x66ooter_row_vertical_stroke\x18\x39 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12?\n#table_body_horizontal_border_stroke\x18: \x01(\x0b\x32\x12.TSD.StrokeArchive\x12=\n!table_body_vertical_border_stroke\x18; \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x38\n\x1ctable_body_horizontal_stroke\x18< \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1atable_body_vertical_stroke\x18= \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1a\x63\x61tegory_level1_top_stroke\x18> \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1a\x63\x61tegory_level2_top_stroke\x18? \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1a\x63\x61tegory_level3_top_stroke\x18@ \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1a\x63\x61tegory_level4_top_stroke\x18\x41 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x36\n\x1a\x63\x61tegory_level5_top_stroke\x18\x42 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1d\x63\x61tegory_level1_bottom_stroke\x18\x43 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1d\x63\x61tegory_level2_bottom_stroke\x18\x44 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1d\x63\x61tegory_level3_bottom_stroke\x18\x45 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1d\x63\x61tegory_level4_bottom_stroke\x18\x46 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1d\x63\x61tegory_level5_bottom_stroke\x18G \x01(\x0b\x32\x12.TSD.StrokeArchive\x12;\n\x1f\x63\x61tegory_level1_interior_stroke\x18H \x01(\x0b\x32\x12.TSD.StrokeArchive\x12;\n\x1f\x63\x61tegory_level2_interior_stroke\x18I \x01(\x0b\x32\x12.TSD.StrokeArchive\x12;\n\x1f\x63\x61tegory_level3_interior_stroke\x18J \x01(\x0b\x32\x12.TSD.StrokeArchive\x12;\n\x1f\x63\x61tegory_level4_interior_stroke\x18K \x01(\x0b\x32\x12.TSD.StrokeArchive\x12;\n\x1f\x63\x61tegory_level5_interior_stroke\x18L \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&category_level1_label_separator_stroke\x18M \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&category_level2_label_separator_stroke\x18N \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&category_level3_label_separator_stroke\x18O \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&category_level4_label_separator_stroke\x18P \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&category_level5_label_separator_stroke\x18Q \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x44\n(table_body_pivot_group_horizontal_stroke\x18R \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&table_body_pivot_group_vertical_stroke\x18S \x01(\x0b\x32\x12.TSD.StrokeArchive\x12I\n-table_body_pivot_deemphasis_horizontal_stroke\x18T \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x45\n)table_body_pivot_emphasis_vertical_stroke\x18U \x01(\x0b\x32\x12.TSD.StrokeArchive\x12G\n+header_column_pivot_group_horizontal_stroke\x18V \x01(\x0b\x32\x12.TSD.StrokeArchive\x12G\n+header_column_pivot_group_deemphasis_stroke\x18W \x01(\x0b\x32\x12.TSD.StrokeArchive\x12@\n$header_column_pivot_separator_stroke\x18X \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&header_row_pivot_group_vertical_stroke\x18Y \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x44\n(header_row_pivot_group_deemphasis_stroke\x18Z \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x39\n\x1dheader_row_pivot_title_stroke\x18[ \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\x42\n&footer_row_pivot_group_vertical_stroke\x18\\ \x01(\x0b\x32\x12.TSD.StrokeArchive\"n\n\x17TableStylePresetArchive\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x1d\n\x05image\x18\x02 \x01(\x0b\x32\x0e.TSP.Reference\x12%\n\rstyle_network\x18\x03 \x01(\x0b\x32\x0e.TSP.Reference\")\n\x18TableStrokePresetArchive\x12\r\n\x05index\x18\x01 \x02(\x05\"\xb6\x01\n\x13ThemePresetsArchive\x12+\n\x13table_style_presets\x18\x01 \x03(\x0b\x32\x0e.TSP.Reference\x12\x31\n\x19table_cell_stroke_presets\x18\x02 \x03(\x0b\x32\x0e.TSP.Reference2?\n\textension\x12\x11.TSS.ThemeArchive\x18\xc8\x01 \x01(\x0b\x32\x18.TST.ThemePresetsArchive')



_DEPRECATED_TABLESTROKEARCHIVE = DESCRIPTOR.message_types_by_name['Deprecated_TableStrokeArchive']
_CELLSTYLEPROPERTIESARCHIVE = DESCRIPTOR.message_types_by_name['CellStylePropertiesArchive']
_DEPRECATED_STROKEPRESETDATAARCHIVE = DESCRIPTOR.message_types_by_name['Deprecated_StrokePresetDataArchive']
_STROKEPRESETDATAARCHIVE = DESCRIPTOR.message_types_by_name['StrokePresetDataArchive']
_STROKEPRESETLISTARCHIVE = DESCRIPTOR.message_types_by_name['StrokePresetListArchive']
_TABLESTYLEPROPERTIESARCHIVE = DESCRIPTOR.message_types_by_name['TableStylePropertiesArchive']
_TABLESTYLEPRESETARCHIVE = DESCRIPTOR.message_types_by_name['TableStylePresetArchive']
_TABLESTROKEPRESETARCHIVE = DESCRIPTOR.message_types_by_name['TableStrokePresetArchive']
_THEMEPRESETSARCHIVE = DESCRIPTOR.message_types_by_name['ThemePresetsArchive']
Deprecated_TableStrokeArchive = _reflection.GeneratedProtocolMessageType('Deprecated_TableStrokeArchive', (_message.Message,), {
  'DESCRIPTOR' : _DEPRECATED_TABLESTROKEARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.Deprecated_TableStrokeArchive)
  })
_sym_db.RegisterMessage(Deprecated_TableStrokeArchive)

CellStylePropertiesArchive = _reflection.GeneratedProtocolMessageType('CellStylePropertiesArchive', (_message.Message,), {
  'DESCRIPTOR' : _CELLSTYLEPROPERTIESARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.CellStylePropertiesArchive)
  })
_sym_db.RegisterMessage(CellStylePropertiesArchive)

Deprecated_StrokePresetDataArchive = _reflection.GeneratedProtocolMessageType('Deprecated_StrokePresetDataArchive', (_message.Message,), {
  'DESCRIPTOR' : _DEPRECATED_STROKEPRESETDATAARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.Deprecated_StrokePresetDataArchive)
  })
_sym_db.RegisterMessage(Deprecated_StrokePresetDataArchive)

StrokePresetDataArchive = _reflection.GeneratedProtocolMessageType('StrokePresetDataArchive', (_message.Message,), {
  'DESCRIPTOR' : _STROKEPRESETDATAARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.StrokePresetDataArchive)
  })
_sym_db.RegisterMessage(StrokePresetDataArchive)

StrokePresetListArchive = _reflection.GeneratedProtocolMessageType('StrokePresetListArchive', (_message.Message,), {
  'DESCRIPTOR' : _STROKEPRESETLISTARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.StrokePresetListArchive)
  })
_sym_db.RegisterMessage(StrokePresetListArchive)

TableStylePropertiesArchive = _reflection.GeneratedProtocolMessageType('TableStylePropertiesArchive', (_message.Message,), {
  'DESCRIPTOR' : _TABLESTYLEPROPERTIESARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.TableStylePropertiesArchive)
  })
_sym_db.RegisterMessage(TableStylePropertiesArchive)

TableStylePresetArchive = _reflection.GeneratedProtocolMessageType('TableStylePresetArchive', (_message.Message,), {
  'DESCRIPTOR' : _TABLESTYLEPRESETARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.TableStylePresetArchive)
  })
_sym_db.RegisterMessage(TableStylePresetArchive)

TableStrokePresetArchive = _reflection.GeneratedProtocolMessageType('TableStrokePresetArchive', (_message.Message,), {
  'DESCRIPTOR' : _TABLESTROKEPRESETARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.TableStrokePresetArchive)
  })
_sym_db.RegisterMessage(TableStrokePresetArchive)

ThemePresetsArchive = _reflection.GeneratedProtocolMessageType('ThemePresetsArchive', (_message.Message,), {
  'DESCRIPTOR' : _THEMEPRESETSARCHIVE,
  '__module__' : 'TSTStylePropertyArchiving_pb2'
  # @@protoc_insertion_point(class_scope:TST.ThemePresetsArchive)
  })
_sym_db.RegisterMessage(ThemePresetsArchive)

if _descriptor._USE_C_DESCRIPTORS == False:
  TSSArchives__pb2.ThemeArchive.RegisterExtension(_THEMEPRESETSARCHIVE.extensions_by_name['extension'])

  DESCRIPTOR._options = None
  _DEPRECATED_TABLESTROKEARCHIVE.fields_by_name['background']._options = None
  _DEPRECATED_TABLESTROKEARCHIVE.fields_by_name['background']._serialized_options = b'\030\001'
  _DEPRECATED_TABLESTROKEARCHIVE.fields_by_name['opacity']._options = None
  _DEPRECATED_TABLESTROKEARCHIVE.fields_by_name['opacity']._serialized_options = b'\030\001'
  _DEPRECATED_TABLESTROKEARCHIVE.fields_by_name['empty']._options = None
  _DEPRECATED_TABLESTROKEARCHIVE.fields_by_name['empty']._serialized_options = b'\030\001'
  _DEPRECATED_TABLESTROKEARCHIVE._serialized_start=137
  _DEPRECATED_TABLESTROKEARCHIVE._serialized_end=268
  _CELLSTYLEPROPERTIESARCHIVE._serialized_start=271
  _CELLSTYLEPROPERTIESARCHIVE._serialized_end=862
  _DEPRECATED_STROKEPRESETDATAARCHIVE._serialized_start=865
  _DEPRECATED_STROKEPRESETDATAARCHIVE._serialized_end=1152
  _STROKEPRESETDATAARCHIVE._serialized_start=1155
  _STROKEPRESETDATAARCHIVE._serialized_end=1339
  _STROKEPRESETLISTARCHIVE._serialized_start=1342
  _STROKEPRESETLISTARCHIVE._serialized_end=1496
  _TABLESTYLEPROPERTIESARCHIVE._serialized_start=1499
  _TABLESTYLEPROPERTIESARCHIVE._serialized_end=6411
  _TABLESTYLEPRESETARCHIVE._serialized_start=6413
  _TABLESTYLEPRESETARCHIVE._serialized_end=6523
  _TABLESTROKEPRESETARCHIVE._serialized_start=6525
  _TABLESTROKEPRESETARCHIVE._serialized_end=6566
  _THEMEPRESETSARCHIVE._serialized_start=6569
  _THEMEPRESETSARCHIVE._serialized_end=6751
# @@protoc_insertion_point(module_scope)
