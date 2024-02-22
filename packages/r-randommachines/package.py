# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandommachines(RPackage):
	"""An Ensemble Modeling using Random Machines

	A novel ensemble method employing Support Vector Machines (SVMs) as base learners. This powerful ensemble model is designed for both classification (Ara A., et. al, 2021) <doi:10.6339/21-JDS1014>, and regression (Ara A., et. al, 2021) <doi:10.1016/j.eswa.2022.117107> problems, offering versatility and robust performance across different datasets and compared with other consolidated methods as Random Forests (Maia M, et. al, 2021) <doi:10.6339/21-JDS1025>.
	"""
	
	cran = "randomMachines" 

	version("0.1.0", md5="cee2f912baea9d41e49abf99ba5d69fe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
