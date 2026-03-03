# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFermicatsr(RPackage):
	"""Fermi Large Area Telescope Catalogs

	Data from various catalogs of astrophysical gamma-ray sources
    detected by NASA's Large Area Telescope (The Astrophysical Journal, 697, 1071,
    2009 June 1), on board the Fermi gamma-ray satellite. More information on
    Fermi and its data products is available from the Fermi Science Support Center
    (http://fermi.gsfc.nasa.gov/ssc/).
	"""
	
	homepage = "https://github.com/sazpark/fermicatsR.git"
	cran = "fermicatsR" 

	version("1.4", md5="90f1b8fc376dcd1fc54ea918f23526f9")

	depends_on("r@3.1:", type=("build", "run"))
