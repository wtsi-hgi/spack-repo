# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabeler(RPackage):
	"""Automate the Production of Custom Labels, Badges, Certificates,
and Other Documents

	Create custom labels, badges, certificates
  and other documents. Automate the production of potentially large 
  numbers of accreditation badges, attendance and participation certificates, 
  herbarium and collection labels, etc. Documents are generated in PDF format, 
  which requires a working installation of 'LaTeX', such as 'TinyTeX'.
	"""
	
	homepage = "https://github.com/EcologyR/labeleR/"
	cran = "labeleR" 

	version("0.1.2", md5="851a7501663bfd761ed45cb02e4814ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
