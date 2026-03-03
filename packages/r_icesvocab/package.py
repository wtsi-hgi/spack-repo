# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesvocab(RPackage):
	"""ICES Vocabularies Database Web Services

	R interface to access the RECO POX web services of the ICES
  (International Council for the Exploration of the Sea) Vocabularies database
  <https://vocab.ices.dk/services/POX.aspx>.
	"""
	
	homepage = "https://vocab.ices.dk/services/POX.aspx"
	cran = "icesVocab" 

	version("1.2.0", md5="00aa9eaa658fe0ae131517cf16222afb")

	depends_on("r-xml2", type=("build", "run"))
