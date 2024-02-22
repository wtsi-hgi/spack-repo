# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQr(RPackage):
	"""QR Factorization without Pivoting

	This function performs QR factorization without pivoting to a real or complex matrix. It is based on Anderson. E. and ten others (1999) "LAPACK Users' Guide". Third Edition. SIAM.
	"""
	
	homepage = "http://www.netlib.org/lapack/explore-html/df/dc5/group__variants_g_ecomputational_ga3766ea903391b5cf9008132f7440ec7b.html"
	cran = "QR" 

	version("0.1.3", md5="a0761bde683ad5baa6fcb54862817164")

	depends_on("r-tinytest", type=("build", "run"))
