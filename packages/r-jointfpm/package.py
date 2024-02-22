# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointfpm(RPackage):
	"""A Parametric Model for Estimating the Mean Number of Events

	Implementation of a parametric joint model for modelling recurrent
  and competing event processes using generalised survival models. The joint
  model can subsequently be used to predict the mean number of events in the
  presence of competing risks at different time points. Comparisons of the mean
  number of event functions, e.g. the differences in mean number of events
  between two exposure groups, are also available.
	"""
	
	homepage = "https://github.com/entjos/JointFPM"
	cran = "JointFPM" 

	version("1.2.0", md5="028cb08cd9236e766144b9b0b36ec651")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rstpm2@1.5.2:", type=("build", "run"))
	depends_on("r-survival@3.2.13:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
