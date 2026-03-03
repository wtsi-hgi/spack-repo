# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaldiquantforeign(RPackage):
	"""Import/Export Routines for 'MALDIquant'

	Functions for reading (tab, csv, Bruker fid, Ciphergen
        XML, mzXML, mzML, imzML, Analyze 7.5, CDF, mMass MSD) and
        writing (tab, csv, mMass MSD, mzML, imzML) different file
        formats of mass spectrometry data into/from 'MALDIquant'
        objects.
	"""
	
	homepage = "https://strimmerlab.github.io/software/maldiquant/"
	cran = "MALDIquantForeign" 

	version("0.14.1", md5="7188c572f2439c388947b7c0fc5bd189")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-maldiquant@1.16.4:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-readbrukerflexdata@1.7:", type=("build", "run"))
	depends_on("r-readmzxmldata@2.7:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
