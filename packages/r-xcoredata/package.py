# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXcoredata(RPackage):
	"""data package for xcore

	Provides data to use with xcore package.
	"""
	
	bioc = "xcoredata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/xcoredata_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/xcoredata/xcoredata_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="e6dfc1d68700e111ef55e136fbb3646e512168d59088e452c007d0e6a8970cb2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub@2.2:", type=("build", "run"))

