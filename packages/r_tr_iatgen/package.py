# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrIatgen(RPackage):
	"""Translate 'iatgen' Generated QSF Files

	Automates translating the instructions of 'iatgen' generated qsf
             (Qualtrics survey files) to other languages using either officially
             supported or user-supplied translations (for tutorial see Santos
             et al., 2023 <doi:10.17504/protocols.io.kxygx34jdg8j/v1>).
	"""
	
	homepage = "https://github.com/iatgen/tr.iatgen"
	cran = "tr.iatgen" 

	version("1.0.0", md5="50a7337d406ab848529fdbd95e06bf7f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
