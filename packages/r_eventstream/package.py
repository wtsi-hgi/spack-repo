# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventstream(RPackage):
	"""Streaming Events and their Early Classification

	Implements event extraction and early classification of events in data streams in R. 
    It has the functionality to generate 2-dimensional data streams with events belonging to 
    2 classes. These events can be extracted and features computed. The event features extracted
    from incomplete-events can be classified using a partial-observations-classifier 
    (Kandanaarachchi et al. 2018) <doi:10.1371/journal.pone.0236331>. 
	"""
	
	homepage = "https://sevvandi.github.io/eventstream/index.html"
	cran = "eventstream" 

	version("0.1.1", md5="807640017d93ceb069b119ea043748f2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-tensora", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
