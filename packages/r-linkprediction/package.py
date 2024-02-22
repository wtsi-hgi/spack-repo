# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkprediction(RPackage):
	"""Link Prediction Methods

	Implementations of most of the existing proximity-based methods of 
  link prediction in graphs. Among the 20 implemented methods are e.g.:
  Adamic L. and Adar E. (2003) <doi:10.1016/S0378-8733(03)00009-1>,
  Leicht E., Holme P., Newman M. (2006) <doi:10.1103/PhysRevE.73.026120>,
  Zhou T. and Zhang Y (2009) <doi:10.1140/epjb/e2009-00335-8>, and
  Fouss F., Pirotte A., Renders J., and Saerens M. (2007) <doi:10.1109/TKDE.2007.46>.
	"""
	
	homepage = "https://github.com/recon-icm/linkprediction"
	cran = "linkprediction" 

	version("1.0-0", md5="d33d4bbc4cff9bf6b3fe6dd179df96fa")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
