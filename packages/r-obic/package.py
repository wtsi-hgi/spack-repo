# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObic(RPackage):
	"""Calculate the Open Bodem Index (OBI) Score

	The Open Bodem Index (OBI) is a method to evaluate the quality of soils of agricultural fields in The Netherlands and the sustainability of the current agricultural practices.
    The OBI score is based on four main criteria: chemical, physical, biological and management, which consist of more than 21 indicators. 
    By providing results of a soil analysis and management info the 'OBIC' package can be use to calculate he scores, indicators and derivatives that are used by the OBI.
    More information about the Open Bodem Index can be found at <https://openbodemindex.nl/>.
	"""
	
	homepage = "https://github.com/AgroCares/Open-Bodem-Index-Calculator"
	cran = "OBIC" 

	version("3.0.1", md5="bae19763ab1cc22f473e6105d14ef335")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
