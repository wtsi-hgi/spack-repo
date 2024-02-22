# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmdbr(RPackage):
	"""IBM in-Database Analytics for R

	
        Functionality required to efficiently use R with IBM(R) Db2(R)
        Warehouse offerings (formerly IBM dashDB(R)) and IBM Db2 for z/OS(R) in
        conjunction with IBM Db2 Analytics Accelerator for z/OS.
        Many basic and complex R operations are pushed down into the database, 
        which removes the main memory boundary of R and allows to make full 
        use of parallel processing in the underlying database.
        For executing R-functions in a multi-node environment in parallel the idaTApply() function
        requires the 'SparkR' package (<https://spark.apache.org/docs/latest/sparkr.html>).
        The optional 'ggplot2' package is needed for the plot.idaLm() function only.
	"""
	
	cran = "ibmdbR" 

	version("1.51.0", md5="e3b146f9e3dfd426a2c3f19408936fc3")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
