# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsimulatr(RPackage):
	"""A Quantum Computer Simulator

	A quantum computer simulator framework with up to 24 qubits. It allows to
    define general single qubit gates and general controlled single
    qubit gates. For convenience, it currently provides the
    most common gates (X, Y, Z, H, Z, S, T, Rx, Ry, Rz, CNOT, SWAP, Toffoli or
    CCNOT, Fredkin or CSWAP). 'qsimulatR' also implements noise models.
    'qsimulatR' supports plotting of circuits and is able to
    export circuits to 'Qiskit' <https://qiskit.org/>, a python package
    which can be used to run on IBM's hardware <https://quantum-computing.ibm.com/>.
	"""
	
	homepage = "https://github.com/HISKP-LQCD/qsimulatR"
	cran = "qsimulatR" 

	version("1.1.1", md5="2a1fd70315bd42c972054b511d2638ca")

