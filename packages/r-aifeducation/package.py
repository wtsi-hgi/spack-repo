# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAifeducation(RPackage):
	"""Artificial Intelligence for Education

	In social and educational settings, the use of Artificial
    Intelligence (AI) is a challenging task. Relevant data is often only
    available in handwritten forms, or the use of data is restricted by
    privacy policies. This often leads to small data sets. Furthermore, in the educational and social sciences,
    data is often unbalanced in terms of
    frequencies. To support educators as well as educational and social
    researchers in using the potentials of AI for their work, this package
    provides a unified interface for neural nets in 'keras',
    'tensorflow', and 'pytorch' to deal with natural language problems. In addition,
    the package ships with a shiny app, providing a graphical user interface.
    This allows the usage of AI for people without skills in writing python/R scripts.
    The tools integrate existing mathematical and statistical methods for dealing
    with small data sets via pseudo-labeling (e.g. Lee (2013)
    <https://www.researchgate.net/publication/280581078_Pseudo-Label_The_Simple_and_Efficient_Semi-Supervised_Learning_Method_for_Deep_Neural_Networks>,
    Cascante-Bonilla et al. (2020) <doi:10.48550/arXiv.2001.06001>) and
    imbalanced data via the creation of synthetic cases (e.g.
    Bunkhumpornpat et al. (2012) <doi:10.1007/s10489-011-0287-y>).
    Performance evaluation of AI is connected to measures from content
    analysis which educational and social researchers are generally more
    familiar with (e.g. Berding & Pargmann (2022) <doi:10.30819/5581>,
    Gwet (2014) <ISBN:978-0-9708062-8-4>, Krippendorff (2019)
    <doi:10.4135/9781071878781>). Estimation of energy consumption and CO2
    emissions during model training is done with the 'python' library
    'codecarbon'.  Finally, all objects created with this package allow to
    share trained AI models with other people.
	"""
	
	homepage = "https://fberding.github.io/aifeducation/"
	cran = "aifeducation" 

	version("0.3.1", md5="b0e7426e3facb6b0867b1969484afd1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-iotarelr@0.1.5:", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-irrcac", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-reticulate@1.34:", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
