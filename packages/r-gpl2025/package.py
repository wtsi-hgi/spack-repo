# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpl2025(RPackage):
	"""Convert Chip ID of the GPL2015 into GeneBank Accession and
ENTREZID

	Convert the chip ID of GPL2025 <https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL2025> 
    to GeneBank Accession and ENTREZID <http://www.ncbi.nlm.nih.gov/gene>.
	"""
	
	cran = "GPL2025" 

	version("1.0.1", md5="6307cd680fe677aaf6b182658d7587f7", url="https://cran.r-project.org/src/contrib/GPL2025_1.0.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
