# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStjudem(RPackage):
	"""Microarray Data from Yeoh et al. in MACAT format

	This is a microarray data set on acute lymphoblastic leukemia, published in 2002 (Yeoh et al.Cancer Cell 2002). The experiments were conducted in the St.Jude Children's Research Hospital, Memphis, Tenessee, USA. The raw data was preprocessed by variance stabilizing normalization (Huber et al.) on probe and subsequent summarization of probe expression values into probe set expression values using median polish.
	"""
	
	bioc = "stjudem"

	version("1.42.0", commit="356d8ad9a1e96d35575214f15b492549669b7073")

	depends_on("r@2.10:", type=("build", "run"))

