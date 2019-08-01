#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):

        # 66 0f 38 25 /r
        # PMOVSXBW xmm1, xmm2/m64

        Buffer = '660f382590'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x0f3825)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pmovsxdq ')
        assert_equal(myDisasm.infos.repr, 'pmovsxdq xmm2, qword ptr [rax+00000000h]')

        # VEX.128.66.0F38.WIG 25 /r
        # vpmovsxdq xmm1, xmm2/m64

        myVEX = VEX('VEX.128.66.0F38.WIG')
        Buffer = '{}2590'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxdq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxdq xmm10, qword ptr [r8+00000000h]')

        # VEX.256.66.0F38.WIG 25 /r
        # vpmovsxdq ymm1, xmm2/m128

        myVEX = VEX('VEX.256.66.0F38.WIG')
        Buffer = '{}2590'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxdq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxdq ymm10, xmmword ptr [r8+00000000h]')

        # EVEX.128.66.0F38.WIG 25 /r
        # vpmovsxdq xmm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.128.66.0F38.WIG')
        Buffer = '{}2590'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxdq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxdq xmm2, qword ptr [rax+00000000h]')

        # EVEX.256.66.0F38.WIG 25 /r
        # vpmovsxdq ymm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.256.66.0F38.WIG')
        Buffer = '{}2590'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxdq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxdq ymm2, xmmword ptr [rax+00000000h]')

        # EVEX.512.66.0F38.WIG 25 /r
        # vpmovsxdq zmm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.512.66.0F38.WIG')
        Buffer = '{}2590'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxdq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxdq zmm2, ymmword ptr [rax+00000000h]')

        # EVEX.128.F3.0F38.W0 25 /r
        # vpmovsqd xmm1/m64 {k1}{z},xmm2

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        Buffer = '{}2590'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsqd ')
        assert_equal(myDisasm.infos.repr, 'vpmovsqd qword ptr [rax+00000000h], xmm2')

        # EVEX.256.F3.0F38.W0 25 /r
        # vpmovsqd xmm1/m128 {k1}{z},ymm2

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        Buffer = '{}2590'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsqd ')
        assert_equal(myDisasm.infos.repr, 'vpmovsqd xmmword ptr [rax+00000000h], ymm2')

        # EVEX.512.F3.0F38.W0 25 /r
        # vpmovsqd ymm1/m256 {k1}{z},zmm2

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}2590'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x25)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsqd ')
        assert_equal(myDisasm.infos.repr, 'vpmovsqd ymmword ptr [rax+00000000h], zmm2')
