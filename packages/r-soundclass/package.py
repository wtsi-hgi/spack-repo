# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoundclass(RPackage):
	"""Sound Classification Using Convolutional Neural Networks

	Provides an all-in-one solution for automatic classification of 
    sound events using convolutional neural networks (CNN). The main purpose 
    is to provide a sound classification workflow, from annotating sound events
    in recordings to training and automating model usage in real-life
    situations. Using the package requires a pre-compiled collection of 
    recordings with sound events of interest and it can be employed for: 
    1) Annotation: create a database of annotated recordings, 
    2) Training: prepare train data from annotated recordings and fit CNN models, 
    3) Classification: automate the use of the fitted model for classifying 
    new recordings. By using automatic feature selection and a user-friendly GUI
    for managing data and training/deploying models, this package is intended 
    to be used by a broad audience as it does not require specific expertise in 
    statistics, programming or sound analysis. Please refer to the vignette for
    further information.
    Gibb, R., et al. (2019) <doi:10.1111/2041-210X.13101>
    Mac Aodha, O., et al. (2018) <doi:10.1371/journal.pcbi.1005995>
    Stowell, D., et al. (2019) <doi:10.1111/2041-210X.13103>
    LeCun, Y., et al. (2012) <doi:10.1007/978-3-642-35289-8_3>.
	"""
	
	cran = "soundClass" 

	version("0.0.9.2", md5="cb7147b9f7d55e0a854092f3a0e314d9")

	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
