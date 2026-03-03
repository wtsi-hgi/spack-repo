# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaekernel(RPackage):
	"""Small Area Estimation Non-Parametric Based Nadaraya-Watson
Kernel

	Propose an area-level, non-parametric regression estimator based on Nadaraya-Watson kernel on small area mean. Adopt a two-stage estimation approach proposed by Prasad and Rao (1990). Mean Squared Error (MSE) estimators are not readily available, so resampling method that called bootstrap is applied. This package are based on the model proposed in Two stage non-parametric approach for small area estimation by Pushpal Mukhopadhyay and Tapabrata Maiti(2004) <http://www.asasrms.org/Proceedings/y2004/files/Jsm2004-000737.pdf>.
	"""
	
	homepage = "https://github.com/wicaksh/saekernel"
	cran = "saekernel" 

	version("0.1.1", md5="a9167b1cc857f40b5daf3a612af4be70")

	depends_on("r@2.10:", type=("build", "run"))
