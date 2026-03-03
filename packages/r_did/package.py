# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDid(RPackage):
	"""Treatment Effects with Multiple Periods and Groups

	The standard Difference-in-Differences (DID) setup involves two periods and two groups -- a treated group and untreated group.  Many applications of DID methods involve more than two periods and have individuals that are treated at different points in time.  This package contains tools for computing average treatment effect parameters in Difference in Differences setups with more than two periods and with variation in treatment timing using the methods developed in Callaway and Sant'Anna (2021) <doi:10.1016/j.jeconom.2020.12.001>.  The main parameters are group-time average treatment effects which are the average treatment effect for a particular group at a a particular time.  These can be aggregated into a fewer number of treatment effect parameters, and the package deals with the cases where there is selective treatment timing, dynamic treatment effects, calendar time effects, or combinations of these.  There are also functions for testing the Difference in Differences assumption, and plotting group-time average treatment effects.
	"""
	
	homepage = "https://bcallaway11.github.io/did/"
	cran = "did" 

	version("2.1.2", md5="34963b4061ac97eefd0c3c69725a5acf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bmisc@1.4.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-drdid", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
