# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslFsa(RPackage):
	"""Fragmentation Spectra Analysis (FSA)

	The 'IDSL.FSA' package was designed to annotate standard .msp (mass spectra format) and .mgf (Mascot generic format) files using mass spectral entropy similarity, dot product (cosine) similarity, and normalized Euclidean mass error (NEME) followed by intelligent pre-filtering steps for rapid spectra searches. 'IDSL.FSA' also provides a number of modules to convert and manipulate .msp and .mgf files. The 'IDSL.FSA' workflow was integrated in the 'IDSL.CSA' and 'IDSL.NPA' packages introduced in <doi:10.1021/acs.analchem.3c00376>.
	"""
	
	homepage = "https://github.com/idslme/idsl.fsa"
	cran = "IDSL.FSA" 

	version("1.2", md5="a6cfa946552e8b7f8e9c9855085b5790")

	depends_on("r@4:", type=("build", "run"))
