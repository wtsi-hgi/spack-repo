# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCritpath(RPackage):
	"""Setting the Critical Path in Project Management

	Solving the problem of project management using CPM (Critical Path Method), PERT (Program Evaluation and Review Technique) and LESS (Least Cost Estimating and Scheduling) methods. The package sets the critical path, schedule and Gantt chart. In addition, it allows to draw a graph even with marked critical activities. For more information about project management see: Taha H. A. "Operations Research. An Introduction" (2017, ISBN:978-1-292-16554-7), Rama Murthy P. "Operations Research" (2007, ISBN:978-81-224-2944-2), Yuval Cohen & Arik Sadeh (2006) "A New Approach for Constructing and Generating AOA Networks", Journal of Engineering, Computing and Architecture 1. 1-13,     Konarzewska I., Jewczak M., Kucharski A. (2020, ISBN:978-83-8220-112-3), Miszczyńska D., Miszczyński M. "Wybrane metody badań operacyjnych" (2000, ISBN:83-907712-0-9).
	"""
	
	cran = "critpath" 

	version("0.2.2", md5="d80108faec951e11fef4a0e0f3bd2c6d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
