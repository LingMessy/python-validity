class DeviceInfo:
    def __init__(self, major: int, type: int, version: int, version_mask: int, name: str):
        self.major, self.type, self.version, self.version_mask, self.name = major, type, version, version_mask, name

    def __repr__(self):
        return "DeviceInfo(0x%04x, 0x%04x, 0x%02x, 0x%02x, '%s')" % (
            self.major, self.type, self.version, self.version_mask, self.name)


dev_info_table = [
    DeviceInfo(0x0000, 0x0080, 0x00, 0x00, 'VSI 15A            '),
    DeviceInfo(0x0000, 0x0080, 0x00, 0x00, 'VSI 15A            '),
    DeviceInfo(0x0000, 0x0080, 0x00, 0x00, 'VSI 15A            '),
    DeviceInfo(0x0000, 0x0083, 0x00, 0x00, 'VSI 40A            '),
    DeviceInfo(0x0000, 0x0083, 0x00, 0x00, 'VSI 40A            '),
    DeviceInfo(0x0000, 0x0083, 0x00, 0x00, 'VSI 40A            '),
    DeviceInfo(0x0000, 0x0080, 0x00, 0x00, 'VSI 15B            '),
    DeviceInfo(0x0000, 0x0080, 0x00, 0x00, 'VSI 15B            '),
    DeviceInfo(0x0000, 0x0080, 0x00, 0x00, 'VSI 15B            '),
    DeviceInfo(0x0000, 0x0089, 0x00, 0x00, 'VSI 32A            '),
    DeviceInfo(0x0000, 0x0089, 0x00, 0x00, 'VSI 32A            '),
    DeviceInfo(0x0000, 0x0089, 0x00, 0x00, 'VSI 32A            '),
    DeviceInfo(0x0049, 0x00b3, 0x01, 0xff, 'SYN 73A0 FM113-001 '),
    DeviceInfo(0x0049, 0x00b3, 0x02, 0xff, 'SYN 73A0 FM125-001 '),
    DeviceInfo(0x0049, 0x00b3, 0x03, 0xff, 'SYN 73A0 FM132-001 '),
    DeviceInfo(0x0049, 0x00b3, 0x04, 0xff, 'SYN 73A0 FM132-002 '),
    DeviceInfo(0x0049, 0x143b, 0x09, 0xff, 'SYN 73A0 FM132-003 '),
    DeviceInfo(0x0049, 0x143b, 0x0a, 0xff, 'SYN 73A0 FM132-004 '),
    DeviceInfo(0x0049, 0x143b, 0x0c, 0xff, 'SYN 73A0 FM132-005 '),
    DeviceInfo(0x0049, 0x00b3, 0x06, 0xff, 'SYN 73A0 FM144-001 '),
    DeviceInfo(0x0049, 0x00b3, 0x07, 0xff, 'SYN 73A0 FM113-002 '),
    DeviceInfo(0x0049, 0x00b3, 0x08, 0xff, 'SYN 73A0 FM159-001 '),
    DeviceInfo(0x0049, 0x143b, 0x0d, 0xff, 'SYN 73A0 FM132-006 '),
    DeviceInfo(0x0049, 0x143b, 0x0e, 0xff, 'SYN 73A0 FM132-007 '),
    DeviceInfo(0x004a, 0x00b5, 0x01, 0xff, 'SYN 57K0           '),
    DeviceInfo(0x004a, 0x0885, 0x02, 0xff, 'SYN 57K1           '),
    DeviceInfo(0x004a, 0x1055, 0x03, 0xff, 'SYN 57K0 HEK       '),
    DeviceInfo(0x004a, 0x00b5, 0x05, 0xff, 'SYN 57K0 Gold1     '),
    DeviceInfo(0x004a, 0x00b5, 0x06, 0xff, 'SYN 57K0 Gold2     '),
    DeviceInfo(0x004a, 0x00b5, 0x07, 0xff, 'SYN 57K0 Gold3     '),
    DeviceInfo(0x004a, 0x00b5, 0x08, 0xff, 'SYN 57K0 Silver    '),
    DeviceInfo(0x004a, 0x00b5, 0x09, 0xff, 'SYN 57K0 FM114-001 '),
    DeviceInfo(0x004a, 0x00b5, 0x0a, 0xff, 'SYN 57K0 FM94-006  '),
    DeviceInfo(0x004a, 0x00b5, 0x0b, 0xff, 'SYN 57K0 FM94-007  '),
    DeviceInfo(0x004a, 0x1825, 0x0c, 0xff, 'SYN 57K0 FM154-001 '),
    DeviceInfo(0x004a, 0x1825, 0x0d, 0xff, 'SYN 57K0 FM155-001 '),
    DeviceInfo(0x004a, 0x1825, 0x0e, 0xff, 'SYN 57K0 FM154-002 '),
    DeviceInfo(0x004a, 0x1825, 0x0f, 0xff, 'SYN 57K0 FM154-003 '),
    DeviceInfo(0x004a, 0x00b5, 0x10, 0xff, 'SYN 57K0 FM94-009  '),
    DeviceInfo(0x004a, 0x00b5, 0x11, 0xff, 'SYN 57K0 FM94-010  '),
    DeviceInfo(0x004a, 0x00b5, 0x12, 0xff, 'SYN 57K0 FM94-011  '),
    DeviceInfo(0x004a, 0x00b5, 0x13, 0xff, 'SYN 57K0 FM3297-02 '),
    DeviceInfo(0x004a, 0x00b5, 0x14, 0xff, 'SYN 57K0 FM3297-03 '),
    DeviceInfo(0x0000, 0x00b5, 0x00, 0x00, 'SYN 57F            '),
    DeviceInfo(0x0000, 0x00b5, 0x00, 0x00, 'SYN 57E            '),
    DeviceInfo(0x0000, 0x00bc, 0x00, 0x00, 'SYN 74A            '),
    DeviceInfo(0x0000, 0x00bc, 0x00, 0x00, 'SYN 74A            '),
    DeviceInfo(0x0000, 0x00be, 0x00, 0x00, 'VSI 19A            '),
    DeviceInfo(0x0000, 0x00be, 0x00, 0x00, 'VSI 19A            '),
    DeviceInfo(0x0000, 0x00be, 0x00, 0x00, 'VSI 19A            '),
    DeviceInfo(0x0000, 0x00c1, 0x00, 0x00, 'VSI 50A            '),
    DeviceInfo(0x0000, 0x00c2, 0x00, 0x00, 'VSI 51A            '),
    DeviceInfo(0x0000, 0x00c3, 0x00, 0x00, 'VSI 50B            '),
    DeviceInfo(0x0000, 0x00c4, 0x00, 0x00, 'VSI 52A            '),
    DeviceInfo(0x0000, 0x00c4, 0x00, 0x00, 'VSI 52A            '),
    DeviceInfo(0x0000, 0x00c4, 0x00, 0x00, 'VSI 52A            '),
    DeviceInfo(0x0000, 0x00ca, 0x00, 0x00, 'VSI 55C            '),
    DeviceInfo(0x0000, 0x00ca, 0x00, 0x00, 'VSI 55A            '),
    DeviceInfo(0x0000, 0x00ca, 0x00, 0x00, 'VSI 55A            '),
    DeviceInfo(0x0000, 0x00cd, 0x00, 0x00, 'VSI 25B            '),
    DeviceInfo(0x0000, 0x00cd, 0x00, 0x00, 'VSI 25B            '),
    DeviceInfo(0x0000, 0x00d1, 0x00, 0x00, 'SYN 110A0          '),
    DeviceInfo(0x0000, 0x00d2, 0x00, 0x00, 'VSI 54A            '),
    DeviceInfo(0x0000, 0x00d3, 0x00, 0x00, 'VSI 59A            '),
    DeviceInfo(0x0000, 0x00d4, 0x00, 0x00, 'VSI 54A            '),
    DeviceInfo(0x0000, 0x00d6, 0x00, 0x00, 'VSI 70A            '),
    DeviceInfo(0x0000, 0x00d7, 0x00, 0x00, 'VSI 71A            '),
    DeviceInfo(0x0070, 0x00da, 0x01, 0xff, 'VSI 55D            '),
    DeviceInfo(0x0071, 0x00db, 0x01, 0xff, 'VSI 55E  FM72-001  '),
    DeviceInfo(0x0071, 0x00db, 0x02, 0xff, 'VSI 55E  FM72-002  '),
    DeviceInfo(0x0071, 0x00db, 0x03, 0xff, 'VSI 55E  FM72-003  '),
    DeviceInfo(0x0071, 0x00db, 0x04, 0xff, 'VSI 55E  FM72-004  '),
    DeviceInfo(0x0071, 0x00db, 0x05, 0xff, 'VSI 55E  FM160-001 '),
    DeviceInfo(0x0071, 0x00db, 0x06, 0xff, 'VSI 55E  FM160-002 '),
    DeviceInfo(0x0071, 0x00db, 0x07, 0xff, 'VSI 55E  FM187-001 '),
    DeviceInfo(0x0071, 0x00db, 0x08, 0xff, 'VSI 55E  FM187-002 '),
    DeviceInfo(0x0071, 0x00db, 0x09, 0xff, 'VSI 55E  FM187-003 '),
    DeviceInfo(0x0071, 0x00db, 0x0a, 0xff, 'VSI 55E  FM160-003 '),
    DeviceInfo(0x0071, 0x04c3, 0x0b, 0xff, 'VSI 55E  FM191-001 '),
    DeviceInfo(0x0071, 0x00db, 0x0c, 0xff, 'VSI 55E  FM187-004 '),
    DeviceInfo(0x0071, 0x00db, 0x0d, 0xff, 'VSI 55E  FM209-001 '),
    DeviceInfo(0x0071, 0x00db, 0x0e, 0xff, 'VSI 55E  FM209-002 '),
    DeviceInfo(0x0071, 0x00db, 0x0f, 0xff, 'VSI 55E  FM3292-001'),
    DeviceInfo(0x0000, 0x00dd, 0x00, 0x00, 'SYN 85A            '),
    DeviceInfo(0x0074, 0x08ae, 0x02, 0xff, 'SYN 109A FM146-001 '),
    DeviceInfo(0x0074, 0x00de, 0x01, 0xff, 'SYN 109A FM146-002 '),
    DeviceInfo(0x0074, 0x00de, 0x03, 0xff, 'SYN 109A FM146-003 '),
    DeviceInfo(0x0074, 0x00de, 0x04, 0xff, 'SYN 109A FM182-001 '),
    DeviceInfo(0x0074, 0x00de, 0x05, 0xff, 'SYN 109A FM192-001 '),
    DeviceInfo(0x0074, 0x00de, 0x06, 0xff, 'SYN 109A FM192-002 '),
    DeviceInfo(0x0074, 0x00de, 0x07, 0xff, 'SYN 109A FM192-003 '),
    DeviceInfo(0x0074, 0x00de, 0x08, 0xff, 'SYN 109A FM192-004 '),
    DeviceInfo(0x0074, 0x00de, 0x09, 0xff, 'SYN 109A FM192-005 '),
    DeviceInfo(0x0074, 0x00de, 0x0a, 0xff, 'SYN 109A FM192-006 '),
    DeviceInfo(0x0074, 0x00de, 0x0b, 0xff, 'SYN 109A FM192-007 '),
    DeviceInfo(0x0074, 0x00de, 0x0c, 0xff, 'SYN 109A FM192-008 '),
    DeviceInfo(0x0074, 0x00de, 0x0d, 0xff, 'SYN 109A FM193-001 '),
    DeviceInfo(0x0074, 0x00de, 0x0e, 0xff, 'SYN 109A FM194-001 '),
    DeviceInfo(0x0074, 0x00de, 0x11, 0xff, 'SYN 109A FM190-003 '),
    DeviceInfo(0x0077, 0x00e1, 0x01, 0xff, 'SYN 75B            '),
    DeviceInfo(0x0077, 0x08b1, 0x03, 0xff, 'SYN 75B0 FM148-001 '),
    DeviceInfo(0x0077, 0x08b1, 0x04, 0xff, 'SYN 75B0 FM148-002 '),
    DeviceInfo(0x0077, 0x08b1, 0x05, 0xff, 'SYN 75B0 FM148-003 '),
    DeviceInfo(0x0077, 0x08b1, 0x06, 0xff, 'SYN 75B0 FM148-004 '),
    DeviceInfo(0x007a, 0x00e4, 0x01, 0xff, 'SYN 57K2 Ofilm     '),
    DeviceInfo(0x007a, 0x00e4, 0x02, 0xff, 'SYN 57K2 ASE       '),
    DeviceInfo(0x007a, 0x00e4, 0x03, 0xff, 'SYN 57K2 FM156-001 '),
    DeviceInfo(0x007f, 0x00b3, 0x01, 0xff, 'SYN 73A1           '),
    DeviceInfo(0x007f, 0x00b3, 0x02, 0xff, 'SYN 73A01 FM152-001'),
    DeviceInfo(0x007f, 0x00b3, 0x03, 0xff, 'SYN 73A01 FM152-002'),
    DeviceInfo(0x007f, 0x00b3, 0x06, 0xff, 'SYN 73A01 FM152-003'),
    DeviceInfo(0x007f, 0x00b3, 0x07, 0xff, 'SYN 73A01 FM152-004'),
    DeviceInfo(0x007f, 0x00b3, 0x04, 0xff, 'SYN 73A01 FM153-001'),
    DeviceInfo(0x007f, 0x00b3, 0x05, 0xff, 'SYN 73A01 FM153-002'),
    DeviceInfo(0x007f, 0x00b3, 0x08, 0xff, 'SYN 73A01 FM153-003'),
    DeviceInfo(0x007f, 0x00b3, 0x09, 0xff, 'SYN 73A01 FM153-004'),
    DeviceInfo(0x007f, 0x00b3, 0x0a, 0xff, 'SYN 73A01 FM152-005'),
    DeviceInfo(0x007f, 0x00b3, 0x0b, 0xff, 'SYN 73A01 FM153-005'),
    DeviceInfo(0x0080, 0x00ea, 0x01, 0xff, 'SYN 77A0 FM133-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x02, 0xff, 'SYN 77A0 FM133-002 '),
    DeviceInfo(0x0080, 0x00ea, 0x03, 0xff, 'SYN 77A0 FM133-003 '),
    DeviceInfo(0x0080, 0x00ea, 0x04, 0xff, 'SYN 77A0 FM-143-001'),
    DeviceInfo(0x0080, 0x00ea, 0x05, 0xff, 'SYN 77A0 FM143-002 '),
    DeviceInfo(0x0080, 0x00ea, 0x06, 0xff, 'SYN 77A0 FM143-003 '),
    DeviceInfo(0x0080, 0x00ea, 0x07, 0xff, 'SYN 77A0 FM147-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x08, 0xff, 'SYN 77A0 FM157-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x09, 0xff, 'SYN 77A0 FM179-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x0a, 0xff, 'SYN 77A0 FM157-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x0b, 0xff, 'SYN 77A0 FM133-004 '),
    DeviceInfo(0x0080, 0x00ea, 0x0c, 0xff, 'SYN 77A0 FM143-004 '),
    DeviceInfo(0x0080, 0x00ea, 0x0d, 0xff, 'SYN 77A0 FM133-005 '),
    DeviceInfo(0x0080, 0x00ea, 0x0e, 0xff, 'SYN 77A0 FM133-006 '),
    DeviceInfo(0x0080, 0x00ea, 0x0f, 0xff, 'SYN 77A0 FM133-007 '),
    DeviceInfo(0x0080, 0x00ea, 0x10, 0xff, 'SYN 77A0 FM143-005 '),
    DeviceInfo(0x0080, 0x00ea, 0x11, 0xff, 'SYN 77A0 FM180-002 '),
    DeviceInfo(0x0080, 0x00ea, 0x13, 0xff, 'SYN 77A0 FM195-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x16, 0xff, 'SYN 77A0 FM232-001 '),
    DeviceInfo(0x0080, 0x00ea, 0x07, 0xff, 'SYN 77B0 FM147-001 '),
    DeviceInfo(0x0083, 0x00ed, 0x01, 0xff, 'SYN 57L            '),
    DeviceInfo(0x0083, 0x00ed, 0x02, 0xff, 'SYN 57L0 FM3299-001'),
    DeviceInfo(0x0083, 0x00ed, 0x03, 0xff, 'SYN 57L0 FM211-001 '),
    DeviceInfo(0x0049, 0x04d5, 0x05, 0xff, 'SYN 57L FM-151-001 '),
    DeviceInfo(0x0049, 0x00ed, 0x0b, 0xff, 'SYN 57L FM-151-002 '),
    DeviceInfo(0x0000, 0x00f6, 0x00, 0x00, 'ENG-UG1-R1         '),
    DeviceInfo(0x0092, 0x00fc, 0x01, 0xff, 'SYN 76A            '),
    DeviceInfo(0x0000, 0x00fd, 0x00, 0x00, 'SYN 79A            '),
    DeviceInfo(0x0000, 0x00fe, 0x00, 0x00, 'SYN 77A            '),
    DeviceInfo(0x0000, 0x00ff, 0x00, 0x00, 'SYN 78A            '),
    DeviceInfo(0x00a4, 0x08de, 0x01, 0xff, 'SYN 82ES           '),
    DeviceInfo(0x0000, 0x0110, 0x00, 0x00, 'SYN 80A            '),
    DeviceInfo(0x0000, 0x0111, 0x00, 0x00, 'SYN 82P            '),
    DeviceInfo(0x0000, 0x0112, 0x00, 0x00, 'SYN 82F            '),
    DeviceInfo(0x0000, 0x0115, 0x00, 0x00, 'SYN 87C            '),
    DeviceInfo(0x00ae, 0x0116, 0x03, 0xff, 'SYN 81D FM119-002  '),
    DeviceInfo(0x00ae, 0x04fe, 0x04, 0xff, 'SYN 81D FM119-003  '),
    DeviceInfo(0x0000, 0x011c, 0x00, 0x00, 'SYN 90A            '),
    DeviceInfo(0x0000, 0x011d, 0x00, 0x00, 'SYN 89A            '),
    DeviceInfo(0x0000, 0x011e, 0x00, 0x00, 'SYN 80A            '),
    DeviceInfo(0x0000, 0x011f, 0x00, 0x00, 'SYN 80A            '),
    DeviceInfo(0x0000, 0x0120, 0x00, 0x00, 'SYN 87D            '),
    DeviceInfo(0x00b7, 0x0b4b, 0x01, 0xff, 'SYN 86C  FM115-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x18, 0xff, 'SYN 86C  FM115-002 '),
    DeviceInfo(0x00b7, 0x0121, 0x13, 0xff, 'SYN 86C  FM115-003 '),
    DeviceInfo(0x00b7, 0x0121, 0x14, 0xff, 'SYN 86C  FM115-004 '),
    DeviceInfo(0x00b7, 0x0b4b, 0x02, 0xff, 'SYN 86C  FM117-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x09, 0xff, 'SYN 86C  FM117-002 '),
    DeviceInfo(0x00b7, 0x0b4c, 0x17, 0xff, 'SYN 86C  FM117-004 '),
    DeviceInfo(0x00b7, 0x0121, 0x1b, 0xff, 'SYN 86C  FM149-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x1c, 0xff, 'SYN 86C  FM149-002 '),
    DeviceInfo(0x00b7, 0x0121, 0x1d, 0xff, 'SYN 86C  FM149-003 '),
    DeviceInfo(0x00b7, 0x0121, 0x1e, 0xff, 'SYN 86C  FM149-004 '),
    DeviceInfo(0x00b7, 0x0121, 0x1f, 0xff, 'SYN 86C  FM149-005 '),
    DeviceInfo(0x00b7, 0x0121, 0x20, 0xff, 'SYN 86C  FM149-006 '),
    DeviceInfo(0x00b7, 0x0121, 0x21, 0xff, 'SYN 86C  FM149-007 '),
    DeviceInfo(0x00b7, 0x0121, 0x22, 0xff, 'SYN 86C  FM149-008 '),
    DeviceInfo(0x00b7, 0x0121, 0x24, 0xff, 'SYN 86C  FM161-001 '),
    DeviceInfo(0x00b7, 0x0b4d, 0x3b, 0xff, 'SYN 86C  FM161-002 '),
    DeviceInfo(0x00b7, 0x0121, 0x26, 0xff, 'SYN 86C  FM163-004 '),
    DeviceInfo(0x00b7, 0x0121, 0x29, 0xff, 'SYN 86C  FM166-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x2a, 0xff, 'SYN 86C  FM166-002 '),
    DeviceInfo(0x00b7, 0x0b4d, 0x2f, 0xff, 'SYN 86C  FM166-003 '),
    DeviceInfo(0x00b7, 0x0b4d, 0x31, 0xff, 'SYN 86C  FM166-005 '),
    DeviceInfo(0x00b7, 0x0b4b, 0x32, 0xff, 'SYN 86C  FM166-006 '),
    DeviceInfo(0x00b7, 0x0121, 0x33, 0xff, 'SYN 86C  FM166-007 '),
    DeviceInfo(0x00b7, 0x0121, 0x3c, 0xff, 'SYN 86C  FM166-008 '),
    DeviceInfo(0x00b7, 0x0121, 0x38, 0xff, 'SYN 86C  FM166-009 '),
    DeviceInfo(0x00b7, 0x0121, 0x3a, 0xff, 'SYN 86C  FM166-011 '),
    DeviceInfo(0x00b7, 0x0121, 0x3d, 0xff, 'SYN 86C  FM166-012 '),
    DeviceInfo(0x00b7, 0x0121, 0x2e, 0xff, 'SYN 86C  FM172-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x34, 0xff, 'SYN 86C  FM172-002 '),
    DeviceInfo(0x00b7, 0x0121, 0x35, 0xff, 'SYN 86C  FM172-003 '),
    DeviceInfo(0x00b7, 0x0121, 0x36, 0xff, 'SYN 86C  FM172-004 '),
    DeviceInfo(0x00b7, 0x0121, 0x42, 0xff, 'SYN 86C  FM224-001 '),
    DeviceInfo(0x00b7, 0x0509, 0x44, 0xff, 'SYN 86C  FM231-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x45, 0xff, 'SYN 86C  FM231-002 '),
    DeviceInfo(0x00b7, 0x0121, 0x4d, 0xff, 'SYN 86C  FM163-005 '),
    DeviceInfo(0x00b7, 0x0121, 0x46, 0xff, 'SYN 86C  FM163-002 '),
    DeviceInfo(0x00b7, 0x0121, 0x47, 0xff, 'SYN 86C  FM163-003 '),
    DeviceInfo(0x00b7, 0x2449, 0x48, 0xff, 'SYN 86C  FM03290001'),
    DeviceInfo(0x00b7, 0x0121, 0x49, 0xff, 'SYN 86C  FM235-001 '),
    DeviceInfo(0x00b7, 0x0121, 0x4a, 0xff, 'SYN 86C  FM235-002 '),
    DeviceInfo(0x00b7, 0x2449, 0x37, 0xff, 'SYN 86C  TM03267001'),
    DeviceInfo(0x0000, 0x0122, 0x00, 0x00, 'SYN 82T4           '),
    DeviceInfo(0x00b9, 0x08f3, 0x04, 0xff, 'SYN 82E1           '),
    DeviceInfo(0x00b9, 0x08f3, 0x05, 0xff, 'SYN 82E2           '),
    DeviceInfo(0x00b9, 0x08f3, 0x06, 0xff, 'SYN 82E3           '),
    DeviceInfo(0x0000, 0x0124, 0x00, 0x00, 'SYN 83A            '),
    DeviceInfo(0x0000, 0x0125, 0x00, 0x00, 'SYN 84C            '),
    DeviceInfo(0x00bc, 0x0126, 0x04, 0xff, 'SYN 86A  FM78-001  '),
    DeviceInfo(0x00bc, 0x0126, 0x05, 0xff, 'SYN 86A  FM78-002  '),
    DeviceInfo(0x00bc, 0x0126, 0x06, 0xff, 'SYN 86A  FM78-003  '),
    DeviceInfo(0x00bc, 0x0126, 0x07, 0xff, 'SYN 86A  FM91-001  '),
    DeviceInfo(0x00bc, 0x0126, 0x0a, 0xff, 'SYN 86A  FM91-002  '),
    DeviceInfo(0x00bc, 0x0126, 0x0b, 0xff, 'SYN 86A  FM91-003  '),
    DeviceInfo(0x00bd, 0x0127, 0x01, 0xff, 'SYN 82E5 FS8203BT12'),
    DeviceInfo(0x0000, 0x012f, 0x00, 0x00, 'SYN 101A           '),
    DeviceInfo(0x00c6, 0x0130, 0x01, 0xff, 'SYN 88B FM141-001  '),
    DeviceInfo(0x00c6, 0x0be1, 0x03, 0xff, 'SYN 88B FM141-003  '),
    DeviceInfo(0x00c6, 0x0be2, 0x05, 0xff, 'SYN 88B FM141-004  '),
    DeviceInfo(0x00c6, 0x0130, 0x06, 0xff, 'SYN 88B FM196-001  '),
    DeviceInfo(0x00c6, 0x0518, 0x07, 0xff, 'SYN 88B FM196-002  '),
    DeviceInfo(0x00c6, 0x0be2, 0x08, 0xff, 'SYN 88B FM196-003  '),
    DeviceInfo(0x00c6, 0x0be1, 0x09, 0xff, 'SYN 88B FM196-004  '),
    DeviceInfo(0x00c6, 0x0130, 0x0b, 0xff, 'SYN 88B FM196-005  '),
    DeviceInfo(0x00c6, 0x0518, 0x0c, 0xff, 'SYN 88B FM196-006  '),
    DeviceInfo(0x00c6, 0x0be2, 0x0d, 0xff, 'SYN 88B FM196-007  '),
    DeviceInfo(0x00c6, 0x0be1, 0x0e, 0xff, 'SYN 88B FM196-008  '),
    DeviceInfo(0x00c6, 0x0518, 0x10, 0xff, 'SYN 88B FM196-009  '),
    DeviceInfo(0x00c6, 0x0518, 0x11, 0xff, 'SYN 88B FM196-010  '),
    DeviceInfo(0x00c6, 0x0be1, 0x0a, 0xff, 'SYN 88B FM205-001  '),
    DeviceInfo(0x00c6, 0x0518, 0x12, 0xff, 'SYN 88B FM241-001  '),
    DeviceInfo(0x00c6, 0x0130, 0x15, 0xff, 'SYN 88B FM241-002  '),
    DeviceInfo(0x00c6, 0x0be2, 0x16, 0xff, 'SYN 88B FM241-003  '),
    DeviceInfo(0x00c6, 0x0be2, 0x17, 0xff, 'SYN 88B FM241-004  '),
    DeviceInfo(0x00c6, 0x0be2, 0x18, 0xff, 'SYN 88B FM241-005  '),
    DeviceInfo(0x00c6, 0x0518, 0x19, 0xff, 'SYN 88B FM241-006  '),
    DeviceInfo(0x00c6, 0x0be2, 0x21, 0xff, 'SYN 88B FM241-007  '),
    DeviceInfo(0x00c6, 0x0518, 0x22, 0xff, 'SYN 88B FM241-008  '),
    DeviceInfo(0x00c6, 0x0518, 0x13, 0xff, 'SYN 88B FM245-001  '),
    DeviceInfo(0x00c6, 0x0518, 0x14, 0xff, 'SYN 88B FM245-002  '),
    DeviceInfo(0x00c6, 0x0130, 0x1a, 0xff, 'SYN 88B FM245-003  '),
    DeviceInfo(0x00c6, 0x0be2, 0x1b, 0xff, 'SYN 88B FM245-004  '),
    DeviceInfo(0x00c6, 0x0518, 0x1d, 0xff, 'SYN 88B FM264-001  '),
    DeviceInfo(0x00c6, 0x0130, 0x1e, 0xff, 'SYN 88B FM264-002  '),
    DeviceInfo(0x00c6, 0x0be2, 0x1f, 0xff, 'SYN 88B FM264-003  '),
    DeviceInfo(0x00c6, 0x0be2, 0x20, 0xff, 'SYN 88B FM264-004  '),
    DeviceInfo(0x00c6, 0x0518, 0x23, 0xff, 'SYN 88B FM264-005  '),
    DeviceInfo(0x0000, 0x016f, 0x00, 0x00, 'VSI 57D            '),
    DeviceInfo(0x0000, 0x016d, 0x00, 0x00, 'VSI 57A            '),
    DeviceInfo(0x0000, 0x016f, 0x00, 0x00, 'VSI 57B            '),
    DeviceInfo(0x0000, 0x016f, 0x00, 0x00, 'VSI 57B            '),
    DeviceInfo(0x0107, 0x0171, 0x01, 0xff, 'SYN 76A            '),
    DeviceInfo(0x0000, 0x0179, 0x00, 0x00, 'ENG VIPER FPGA     '),
    DeviceInfo(0x0000, 0x017c, 0x00, 0x00, 'SYNA 106A          '),
    DeviceInfo(0x0112, 0x017c, 0x01, 0xff, 'SYNA 106A FM225-001'),
    DeviceInfo(0x0114, 0x017e, 0x01, 0x00, 'SYNA 86D           '),
    DeviceInfo(0x011b, 0x0185, 0x02, 0xff, 'SYN 82ES3          '),
    DeviceInfo(0x0190, 0x2449, 0x01, 0xff, '86C  FM-3290-002   '),
    DeviceInfo(0x0190, 0x2449, 0x02, 0xff, '86C  FM-3324-001   '),
    DeviceInfo(0x0190, 0x057b, 0x03, 0xff, '88B0 FM-3316-001   '),
    DeviceInfo(0x0190, 0x1ff5, 0x04, 0xff, '57K0 FM-3328-001   '),
    DeviceInfo(0x0190, 0x00b5, 0x05, 0xff, '57K0 FM-3297-004   '),
    DeviceInfo(0x0190, 0x0c6d, 0x06, 0xff, '57K0 FM-3297-005   '),
    DeviceInfo(0x0190, 0x00b5, 0x07, 0xff, '57K0 FM-3297-006   '),
    DeviceInfo(0x0190, 0x00b5, 0x08, 0xff, '57K0 FM-3297-007   '),
    DeviceInfo(0x0190, 0x00b5, 0x09, 0xff, '57K0 FM-3297-008   '),
    DeviceInfo(0x0190, 0x00b5, 0x0a, 0xff, '57K0 FM-3297-009   '),
    DeviceInfo(0x0190, 0x00b5, 0x0b, 0xff, '57K0 FM-3297-010   '),
    DeviceInfo(0x0190, 0x00b5, 0x0c, 0xff, '57K0 FM-3297-011   '),
    DeviceInfo(0x0190, 0x057b, 0x0d, 0xff, '88B0 FM-3300-001   '),
    DeviceInfo(0x0190, 0x04c3, 0x0e, 0xff, '55E  FM3327-FM3342 '),
    DeviceInfo(0x0190, 0x0191, 0x0f, 0xff, '57L0 FM-3331-001   '),
    DeviceInfo(0x0190, 0x0191, 0x10, 0xff, '57L0 FM-3331-002   '),
    DeviceInfo(0x0190, 0x0191, 0x11, 0xff, '57L0 FM-3331-003   '),
    DeviceInfo(0x0190, 0x0580, 0x12, 0xff, '88B0 FM-3310-001   '),
    DeviceInfo(0x0190, 0x0580, 0x13, 0xff, '88B0 FM-3310-002   '),
    DeviceInfo(0x0190, 0x0191, 0x14, 0xff, '57L0 FM- 151-003   '),
    DeviceInfo(0x0190, 0x0191, 0x15, 0xff, '57L0 FM- 211-002   '),
    DeviceInfo(0x0190, 0x0191, 0x16, 0xff, '57L0 FM-3299-002   '),
    DeviceInfo(0x0190, 0x0d49, 0x17, 0xff, '57L0 FM-3331-004   '),
    DeviceInfo(0x0190, 0x1131, 0x18, 0xff, '57L0 FM-3331-005   '),
    DeviceInfo(0x0190, 0x0197, 0x19, 0xff, '73A0 FM-3332-001   '),
    DeviceInfo(0x0190, 0x0195, 0x1a, 0xff, '86D  TM3329-001-003'),
    DeviceInfo(0x0190, 0x0195, 0x1b, 0xff, '86D  TM3329-002-006'),
    DeviceInfo(0x0190, 0x0196, 0x1c, 0xff, '57K0 FM- 155-003   '),
    DeviceInfo(0x0190, 0x2449, 0x1d, 0xff, '86C  TM-3315-001   '),
    DeviceInfo(0x0190, 0x2449, 0x1e, 0xff, '86C  TM-3315-002   '),
    DeviceInfo(0x0190, 0x2449, 0x1f, 0xff, '86C  TM-3322-001   '),
    DeviceInfo(0x0190, 0x2449, 0x20, 0xff, '86C  FM-3326-001   '),
    DeviceInfo(0x0190, 0x2449, 0x21, 0xff, '86C  FM-3208-002   '),
    DeviceInfo(0x0190, 0x2449, 0x22, 0xff, '86C  FM-3340-001   '),
    DeviceInfo(0x0190, 0x0196, 0x23, 0xff, '57K0 FM- 155-004   '),
    DeviceInfo(0x0190, 0x00b5, 0x24, 0xff, '57K0 FM-3297-012   '),
    DeviceInfo(0x0190, 0x00b5, 0x25, 0xff, '57K0 FM-3297-013   '),
    DeviceInfo(0x0190, 0x0197, 0x26, 0xff, '73A0 FM-3341-001   '),
    DeviceInfo(0x0190, 0x2449, 0x28, 0xff, '86C  TM-3315-003   '),
    DeviceInfo(0x0190, 0x00b5, 0x29, 0xff, '57K0 FM-3297-020   '),
    DeviceInfo(0x0190, 0x00b5, 0x2a, 0xff, '57K0 FM-3297-021   '),
    DeviceInfo(0x0190, 0x00b5, 0x2b, 0xff, '57K0 FM-3297-022   '),
    DeviceInfo(0x0190, 0x00b5, 0x2c, 0xff, '57K0 FM-3297-023   '),
    DeviceInfo(0x0190, 0x00b5, 0x2d, 0xff, '57K0 FM-3297-024   '),
    DeviceInfo(0x0190, 0x00b5, 0x2e, 0xff, '57K0 FM-3297-025   '),
    DeviceInfo(0x0190, 0x00b5, 0x2f, 0xff, '57K0 FM-3297-026   '),
    DeviceInfo(0x0190, 0x00b5, 0x30, 0xff, '57K0 FM-3297-027   '),
    DeviceInfo(0x0190, 0x00b5, 0x31, 0xff, '57K0 FM-3297-028   '),
    DeviceInfo(0x0190, 0x00b5, 0x32, 0xff, '57K0 FM-3297-029   '),
    DeviceInfo(0x0190, 0x00b5, 0x33, 0xff, '57K0 FM-3297-030   '),
    DeviceInfo(0x0190, 0x00b5, 0x34, 0xff, '57K0 FM-3297-031   '),
    DeviceInfo(0x0190, 0x00b5, 0x35, 0xff, '57K0 FM-3297-014   '),
    DeviceInfo(0x0190, 0x00b5, 0x36, 0xff, '57K0 FM-3297-015   '),
    DeviceInfo(0x0190, 0x00b5, 0x37, 0xff, '57K0 FM-3297-032   '),
    DeviceInfo(0x0190, 0x00b5, 0x38, 0xff, '57K0 FM-3297-033   '),
    DeviceInfo(0x0190, 0x057b, 0x39, 0xff, '88B0 FM-3300-002   '),
    DeviceInfo(0x0190, 0x00de, 0x3a, 0xff, '109A_FM-3302-001   '),
    DeviceInfo(0x0190, 0x057e, 0x3b, 0xff, '57K0 FM- 154-020   '),
    DeviceInfo(0x0190, 0x0581, 0x3c, 0xff, '57K0 FM- 154-021   '),
    DeviceInfo(0x0190, 0x2449, 0x3d, 0xff, '86C  TM-3226-001   '),
    DeviceInfo(0x0190, 0x0195, 0x3e, 0xff, '86D  TM3329-004-007'),
    DeviceInfo(0x0190, 0x0196, 0x3f, 0xff, '57K0 FM- 155-002   '),
    DeviceInfo(0x0190, 0x1825, 0x41, 0xff, '57K0 FM- 154-001   '),
    DeviceInfo(0x0190, 0x0581, 0x42, 0xff, '57K0 FM- 154-022   '),
    DeviceInfo(0x0190, 0x057b, 0x43, 0xff, '88B0FM3358-1 3359-2'),
    DeviceInfo(0x0190, 0x057b, 0x44, 0xff, '88B0 FM-3358-002   '),
    DeviceInfo(0x0190, 0x057b, 0x45, 0xff, '88B0 FM-3359-001   '),
    DeviceInfo(0x0190, 0x00b5, 0x46, 0xff, '57K0 FM-3297-100   '),
    DeviceInfo(0x0190, 0x057e, 0x47, 0xff, '57K0 FM- 154-200   '),
    DeviceInfo(0x0190, 0x0000, 0x48, 0xff, '115C0FM-3363-001   '),
    DeviceInfo(0x0190, 0x0198, 0x49, 0xff, '88B0 FM-3366-001   '),
    DeviceInfo(0x0190, 0x0199, 0x4a, 0xff, '57K0 FM-3367-001   '),
    DeviceInfo(0x0190, 0x2449, 0x4b, 0xff, '86C  TM-3368-001   '),
    DeviceInfo(0x0190, 0x00db, 0x4c, 0xff, '55E  FM- 209-005   '),
    DeviceInfo(0x0190, 0x0000, 0x4d, 0xff, '115C0FM-3371-001   '),
    DeviceInfo(0x0190, 0x0000, 0x4e, 0xff, '115C0FM-3372-001   '),
    DeviceInfo(0x0190, 0x0969, 0x4f, 0xff, '57K0 FM- 154-023   '),
    DeviceInfo(0x0190, 0x0580, 0x50, 0xff, '88B0 FM-3373-001   '),
    DeviceInfo(0x0190, 0x00db, 0x51, 0xff, '55E  FM- 209-006   '),
    DeviceInfo(0x0190, 0x0581, 0x52, 0xff, '57K0 FM- 154-001   '),
    DeviceInfo(0x0190, 0x0581, 0x53, 0xff, '57K0 FM- 154-002   '),
    DeviceInfo(0x0190, 0x0581, 0x54, 0xff, '57K0 FM- 154-003   '),
    DeviceInfo(0x0190, 0x0581, 0x55, 0xff, '57K0 FM- 154-020   '),
    DeviceInfo(0x0190, 0x0581, 0x56, 0xff, '57K0 FM- 155-001   '),
    DeviceInfo(0x0190, 0x0199, 0x57, 0xff, '57K0 FM- 155-002   '),
    DeviceInfo(0x0190, 0x0195, 0x58, 0xff, '86D  TM-3329-005   '),
    DeviceInfo(0x0190, 0x0199, 0x59, 0xff, '57K0 FM-3367-002   '),
    DeviceInfo(0x0190, 0x0199, 0x5a, 0xff, '57K0 FM-3367-003   '),
    DeviceInfo(0x0190, 0x0199, 0x5b, 0xff, '57K0 FM-3367-004   '),
    DeviceInfo(0x0190, 0x00db, 0x5c, 0xff, '55E  FM- 160-004   '),
    DeviceInfo(0x0190, 0x0968, 0x5d, 0xff, '88B0 FM-3366-002   '),
    DeviceInfo(0x0190, 0x2449, 0x5e, 0xff, '86C  TM-P3376-P3404'),
    DeviceInfo(0x0190, 0x00b5, 0x5f, 0xff, '57K0 FM-3380-001   '),
    DeviceInfo(0x0190, 0x0199, 0x60, 0xff, '57K0 FM-3380-002   '),
    DeviceInfo(0x0190, 0x0199, 0x61, 0xff, '57K0 FM-3380-003   '),
    DeviceInfo(0x0190, 0x0199, 0x62, 0xff, '57K0 FM-3380-004   '),
    DeviceInfo(0x0190, 0x2449, 0x63, 0xff, '86C  FM-3290-003   '),
    DeviceInfo(0x0190, 0x057b, 0x64, 0xff, '88B0 FM-3358-003   '),
    DeviceInfo(0x0190, 0x2449, 0x65, 0xff, '86C  FM-3389-001   '),
    DeviceInfo(0x0190, 0x0000, 0x66, 0xff, '115C0FM-3363-002   '),
    DeviceInfo(0x0190, 0x0000, 0x67, 0xff, '115C0FM-3363-003   '),
    DeviceInfo(0x0190, 0x0199, 0x68, 0xff, '57K0 FM-3367-005   '),
    DeviceInfo(0x0190, 0x0199, 0x69, 0xff, '57K0 FM-3367-006   '),
    DeviceInfo(0x0190, 0x0199, 0x6a, 0xff, '57K0 FM-3380-001   '),
    DeviceInfo(0x0190, 0x0191, 0x6b, 0xff, '57L0 FM-3396-001   '),
    DeviceInfo(0x0190, 0x0191, 0x6c, 0xff, '57L0 FM-3397-001   '),
    DeviceInfo(0x0190, 0x0000, 0x6d, 0xff, '115C0TM-P3374-100  '),
    DeviceInfo(0x0190, 0x2449, 0x6e, 0xff, '86C  TM3261-003-004'),
    DeviceInfo(0x0190, 0x0581, 0x6f, 0xff, '57K0 FM-3395-001   '),
    DeviceInfo(0x0190, 0x0d51, 0x70, 0xff, '57K0 FM- 154-120   '),
    DeviceInfo(0x0190, 0x0969, 0x71, 0xff, '57K0 FM- 154-123   '),
    DeviceInfo(0x0190, 0x00b5, 0x72, 0xff, '57K0 FM-3401-001   '),
    DeviceInfo(0x0190, 0x00b5, 0x73, 0xff, '57K0 FM-3401-004   '),
    DeviceInfo(0x0190, 0x00b5, 0x74, 0xff, '57K0 FM-3401-005   '),
    DeviceInfo(0x0190, 0x00b5, 0x75, 0xff, '57K0 FM-3401-006   '),
    DeviceInfo(0x0190, 0x0199, 0x76, 0xff, '57K0 FM-155-005/006'),
    DeviceInfo(0x0190, 0x0193, 0x77, 0xff, '88B0 FM-3366-001   '),
    DeviceInfo(0x0190, 0x0d4b, 0x78, 0xff, '88B0 FM-3366-002   '),
    DeviceInfo(0x0190, 0x0c6d, 0x79, 0xff, '57K0 FM-3297-034   '),
    DeviceInfo(0x0190, 0x00b5, 0x7a, 0xff, '57K0 FM-3297-035   '),
    DeviceInfo(0x0190, 0x057b, 0x7b, 0xff, '88B0 FM-3358-004   '),
    DeviceInfo(0x0190, 0x057b, 0x7c, 0xff, '88B0 FM-3358-005   '),
    DeviceInfo(0x0190, 0x0963, 0x7d, 0xff, '88B0 FM-3358-006   '),
    DeviceInfo(0x0190, 0x00de, 0x00, 0xff, '109A_FM-3302-001   '),
    DeviceInfo(0x0190, 0x0199, 0x7e, 0xff, '57K0 FM-155-007    '),
    DeviceInfo(0x0190, 0x0199, 0x82, 0xff, '57K0 FM-155-102    '),
    DeviceInfo(0x0190, 0x00de, 0x7f, 0xff, '109A_FM-3435-001   '),
    DeviceInfo(0x0190, 0x0d51, 0x83, 0xff, '57K0 FM-3439-001   '),
    DeviceInfo(0x0190, 0x2449, 0x84, 0xff, '86C  FM-3324-002   '),
    DeviceInfo(0x0190, 0x0969, 0x85, 0xff, '57K0 FM-3439-002   '),
    DeviceInfo(0x0190, 0x2449, 0x86, 0xff, '86C  FM-3324-003   '),
    DeviceInfo(0x0190, 0x0969, 0x87, 0xff, '57K0 FM-3439-003   '),
    DeviceInfo(0x0190, 0x0969, 0x88, 0xff, '57K0 FM-3439-004   '),
    DeviceInfo(0x0190, 0x0199, 0x89, 0xff, '57K0 FM-155-008    '),
    DeviceInfo(0x0190, 0x0581, 0x8a, 0xff, '57K0 FM-154-124    '),
    DeviceInfo(0x0190, 0x057b, 0x8b, 0xff, '88B0 FM-3358-007   '),
    DeviceInfo(0x0190, 0x0581, 0x8c, 0xff, '57K0 FM-3439-005   '),
    DeviceInfo(0x0190, 0x0969, 0x8d, 0xff, '57K0 FM-3439-006   '),
    DeviceInfo(0x0190, 0x0199, 0x8e, 0xff, '57K0 FM-155-103    '),
    DeviceInfo(0x0190, 0x0581, 0x8f, 0xff, '57K0 FM-154-125    '),
    DeviceInfo(0x0190, 0x0581, 0x90, 0xff, '57K0 FM-3439-007   '),
    DeviceInfo(0x0190, 0x0969, 0x91, 0xff, '57K0 FM-3439-008   '),
    DeviceInfo(0x0190, 0x0969, 0x92, 0xff, '57K0 FM-3439-009   '),
    DeviceInfo(0x0190, 0x0969, 0x93, 0xff, '57K0 FM-3439-010   '),
    DeviceInfo(0x0190, 0x0969, 0x94, 0xff, '57K0 FM-3439-011   '),
    DeviceInfo(0x0190, 0x0969, 0x95, 0xff, '57K0 FM-3439-108   '),
    DeviceInfo(0x0190, 0x0969, 0x96, 0xff, '57K0 FM-3439-109   '),
    DeviceInfo(0x0190, 0x0969, 0x97, 0xff, '57K0 FM-3439-110   '),
    DeviceInfo(0x0190, 0x057b, 0x98, 0xff, '88B0 FM-3358-008   '),
    DeviceInfo(0x0190, 0x057b, 0x99, 0xff, '88B0 FM-3358-009   '),
    DeviceInfo(0x0190, 0x0d51, 0x9a, 0xff, '57K0 FM-3439-101   '),
    DeviceInfo(0x0190, 0x0969, 0x9b, 0xff, '57K0 FM-3439-102   '),
    DeviceInfo(0x0190, 0x0969, 0x9c, 0xff, '57K0 FM-3439-012   '),
    DeviceInfo(0x0190, 0x1139, 0x9d, 0xff, '57K0 FM-3439-013   '),
    DeviceInfo(0x0190, 0x0969, 0x9e, 0xff, '57K0 FM-3439-014   '),
    DeviceInfo(0x0190, 0x0c6d, 0x9f, 0xff, '57K0 FM-3297-036   '),
    DeviceInfo(0x0190, 0x057b, 0xa0, 0xff, '88B0 FM-3358-010   '),
    DeviceInfo(0x0190, 0x057b, 0xa1, 0xff, '88B0 FM-3316-002   '),
    DeviceInfo(0x0190, 0x2449, 0xa2, 0xff, '86C  TM-P3568-001  '),
    DeviceInfo(0x0190, 0x2449, 0xa3, 0xff, '86C  TM-P3569-001  '),
]


def dev_info_lookup(major: int, ver: int):
    fuzzy_match = None

    for i in dev_info_table:
        if i.major != major:
            continue

        masked_ver = i.version & i.version_mask

        if ver == 0 or masked_ver == 0:
            fuzzy_match = i
        elif ver == masked_ver:
            return i

    return fuzzy_match


class FlashIcInfo:
    def __init__(self, name: str, size: int, f18: int, jid0: int, jid1: int, f1b: int, f1c: int,
                 f1e: int, secror_size: int, sector_erase_cmd: int, f25: int, f26: int):
        self.name, self.size, self.f18, self.jid0, self.jid1, self.f1b, self.f1c, self.f1e, self.secror_size, self.sector_erase_cmd, self.f25, self.f26 = name, size, f18, jid0, jid1, f1b, f1c, f1e, secror_size, sector_erase_cmd, f25, f26

    def __repr__(self):
        return "FlashIcInfo('%s', %d, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x)" % (
            self.name, self.size, self.f18, self.jid0, self.jid1, self.f1b, self.f1c, self.f1e,
            self.secror_size, self.sector_erase_cmd, self.f25, self.f26)


flash_ic_table = [
    FlashIcInfo('M25P05-A', 65536, 0x5, 0x20, 0x20, 0x10, 0x8000, 0x0, 0x8000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P10-A', 131072, 0x10, 0x20, 0x20, 0x11, 0x8000, 0x0, 0x8000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P20', 262144, 0x11, 0x20, 0x20, 0x12, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P40', 524288, 0x12, 0x20, 0x20, 0x13, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P80', 1048576, 0x13, 0x20, 0x20, 0x14, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P16', 2097152, 0x14, 0x20, 0x20, 0x15, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P32', 4194304, 0x15, 0x20, 0x20, 0x16, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('M25P64', 8388608, 0x16, 0x20, 0x20, 0x17, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('SST25VF040B', 524288, 0x8d, 0xbf, 0x25, 0x8d, 0x0, 0x1, 0x10000, 0xd8, 0x0, 0x4),
    FlashIcInfo('W25X10A', 131072, 0x10, 0xef, 0x30, 0x11, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('W25X20A', 262144, 0x11, 0xef, 0x30, 0x12, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('W25X40A', 524288, 0x12, 0xef, 0x30, 0x13, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('W25X80A', 1048576, 0x13, 0xef, 0x30, 0x14, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('W25Q40B', 524288, 0x12, 0xef, 0x40, 0x13, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('W25Q80B', 1048576, 0x13, 0xef, 0x40, 0x14, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('MX25L4006E', 524288, 0x12, 0xc2, 0x20, 0x13, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('EN25Q40', 524288, 0x12, 0x1c, 0x30, 0x13, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('MX25V8035F', 1048576, 0x14, 0xc2, 0x23, 0x14, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('AT25SF081', 1048576, 0x14, 0x1f, 0x85, 0x1, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
    FlashIcInfo('GD25Q80C', 1048576, 0x13, 0xc8, 0x40, 0x14, 0x0, 0x1, 0x1000, 0x20, 0x0, 0x4),
]


def flash_ic_table_lookup(jedec_id0: int, jedec_id1: int, size: int):
    for i in flash_ic_table:
        if i.jid0 == jedec_id0 and i.jid1 == jedec_id1 and i.size == size:
            return i

    return None
