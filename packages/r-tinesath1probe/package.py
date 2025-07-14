# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinesath1probe(RPackage):
	"""Probe sequence data for microarrays of type tinesath1

	This package was automatically created by package matchprobes version 1.4.0. The probe sequence data was obtained from http://www.affymetrix.com.
	"""
	
	bioc = "tinesath1probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/tinesath1probe_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/tinesath1probe/tinesath1probe_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="29931479e7a68eff177d7b7a42c2ec4eb893792ea84b37f402380ff0e74f21e8")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.9:", type=("build", "run"))

