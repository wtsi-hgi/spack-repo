# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeebodata(RPackage):
	"""HEEBO set and HEEBO controls.

	R objects describing the HEEBO oligo set.
	"""
	
	homepage = "http://alizadehlab.stanford.edu/"
	bioc = "HEEBOdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HEEBOdata_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HEEBOdata/HEEBOdata_1.40.0.tar.gz"]

	version("1.40.0", sha256="b080c3ff5a90428dd8c6a11a6f605acca315c44075bef09bc721852b46cd32f6")


