# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMschart(RPackage):
	"""Chart Generation for 'Microsoft Word' and 'Microsoft PowerPoint'
Documents

	Create native charts for 'Microsoft PowerPoint' and 'Microsoft Word' documents. 
 These can then be edited and annotated. Functions are provided to let users create charts, modify 
 and format their content. The chart's underlying data is automatically saved within the 
 'Word' document or 'PowerPoint' presentation. It extends package 'officer' that does 
 not contain any feature for 'Microsoft' native charts production. 
	"""
	
	homepage = "https://ardata-fr.github.io/officeverse/"
	cran = "mschart" 

	version("0.4.0", md5="28385fac0ac7794daff7ad7e22393288")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-officer@0.3.6:", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-xml2@1.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
