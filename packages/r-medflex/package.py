# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedflex(RPackage):
	"""Flexible Mediation Analysis Using Natural Effect Models

	Run flexible mediation analyses using natural effect models as described in 
  Lange, Vansteelandt and Bekaert (2012) <DOI:10.1093/aje/kwr525>, 
  Vansteelandt, Bekaert and Lange (2012) <DOI:10.1515/2161-962X.1014> 
  and Loeys, Moerkerke, De Smet, Buysse, Steen and Vansteelandt (2013) <DOI:10.1080/00273171.2013.832132>.
	"""
	
	homepage = "https://github.com/jmpsteen/medflex"
	cran = "medflex" 

	version("0.6-10", md5="17790bde6ef4669a90c8b41a61e2387b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-multcomp@1.3.6:", type=("build", "run"))
	depends_on("r-boot@1.3.8:", type=("build", "run"))
	depends_on("r-car@2.0.21:", type=("build", "run"))
	depends_on("r-matrix@1.1.4:", type=("build", "run"))
	depends_on("r-sandwich@2.3.2:", type=("build", "run"))
