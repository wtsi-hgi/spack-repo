# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRock(RPackage):
	"""Reproducible Open Coding Kit

	The Reproducible Open Coding Kit ('ROCK', and this package, 'rock')
  was developed to facilitate reproducible and open coding, specifically
  geared towards qualitative research methods. Although it is a
  general-purpose toolkit, three specific applications have been
  implemented, specifically an interface to the 'rENA' package that
  implements Epistemic Network Analysis ('ENA'), means to process notes
  from Cognitive Interviews ('CIs'), and means to work with decentralized
  construct taxonomies ('DCTs'). The 'ROCK' and this 'rock' package are described
  in the ROCK book <https://rockbook.org> and more information, such as tutorials,
  is available at <https://rock.science>.
	"""
	
	homepage = "https://rock.opens.science"
	cran = "rock" 

	version("0.8.1", md5="c73be7028c7d53ddc824fca705bbb680")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-tree@1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-htmltools@0.5:", type=("build", "run"))
	depends_on("r-markdown@1.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-yaml@2.2:", type=("build", "run"))
	depends_on("r-yum@0.1:", type=("build", "run"))
