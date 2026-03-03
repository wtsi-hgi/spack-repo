# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabias(RPackage):
	"""Meta-Analysis for Within-Study and/or Across-Study Biases

	Provides common components (classes, methods, documentation) for
  packages that conduct meta-analytic corrections and sensitivity analyses
  for within-study and/or across-study biases in meta-analysis. See the packages
  'PublicationBias', 'phacking', and 'multibiasmeta'. These package implement
  methods described in, respectively: Mathur & VanderWeele (2020)
  <doi:10.31219/osf.io/s9dp6>; Mathur (2022) <doi:10.31219/osf.io/ezjsx>;
  Mathur (2022) <doi:10.31219/osf.io/u7vcb>.
	"""
	
	homepage = "https://github.com/mathurlabstanford/metabias"
	cran = "metabias" 

	version("0.1.1", md5="e066c2170d8078b189fb535e11aabc43")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
