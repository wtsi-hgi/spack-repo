# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomenv(RPackage):
	"""SOM Algorithm for the Analysis of Multivariate Environmental
Data

	Analysis of multivariate environmental high frequency data by Self-Organizing Map and k-means clustering algorithms. By means of the graphical user interface it provides a comfortable way to elaborate by self-organizing map algorithm rather big datasets (txt files up to 100 MB ) obtained by environmental high-frequency monitoring by sensors/instruments. The functions present in the package are based on 'kohonen' and 'openair' packages implemented by functions embedding Vesanto et al. (2001) <http://www.cis.hut.fi/projects/somtoolbox/package/papers/techrep.pdf>  heuristic rules for map initialization parameters, k-means clustering algorithm and map features visualization. Cluster profiles visualization as well as graphs dedicated to the visualization of time-dependent variables Licen et al. (2020) <doi:10.4209/aaqr.2019.08.0414> are provided.
	"""
	
	homepage = "https://github.com/SomEnv/somenv"
	cran = "SOMEnv" 

	version("1.1.2", md5="77e72ea3717cae5be8fc68200d8da27b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
