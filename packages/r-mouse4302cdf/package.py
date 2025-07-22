# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse4302cdf(RPackage):
	"""mouse4302cdf

	A package containing an environment representing the Mouse430_2.cdf file.
	"""
	
	bioc = "mouse4302cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse4302cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse4302cdf/mouse4302cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="8ceb1679dda78943591ccc86c3214d8e09ed18e1fd945eab13da7dd489aafed6")

	depends_on("r-annotationdbi", type=("build", "run"))

