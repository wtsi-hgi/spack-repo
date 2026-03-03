# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwopexp(RPackage):
	"""The Two Parameter Exponential Distribution

	Density, distribution function, quantile function, 
    and random generation function, maximum likelihood estimation (MLE), 
    penalized maximum likelihood estimation (PMLE), the quartiles method estimation (QM),
    and median rank estimation (MEDRANK) for the two-parameter exponential distribution.
    MLE and PMLE are based on Mengjie Zheng (2013)<https://scse.d.umn.edu/sites/scse.d.umn.edu/files/mengjie-thesis_masters-1.pdf>.
    QM is based on Entisar Elgmati and Nadia Gregni (2016)<doi:10.5539/ijsp.v5n5p12>.
    MEDRANK is based on Matthew Reid (2022)<doi:10.5281/ZENODO.3938000>.
	"""
	
	cran = "twopexp" 

	version("0.1.0", md5="b232b20b3bf5bf3a340f0e4e8f06cece")

	depends_on("r@2.10:", type=("build", "run"))
