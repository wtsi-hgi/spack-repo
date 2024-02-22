# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtestclust(RPackage):
	"""Reweighted Marginal Hypothesis Tests for Clustered Data

	A collection of reweighted marginal hypothesis tests for clustered data, based
    on reweighting methods of Williamson, J., Datta, S., and Satten, G. (2003) <doi:10.1111/1541-0420.00005>.
    The tests in this collection are clustered analogs to well-known hypothesis tests
    in the classical setting, and are appropriate for data with cluster- and/or group-size 
    informativeness. The syntax and output of functions are modeled after common, 
    recognizable functions native to R. Methods used in the package refer to 
    Gregg, M., Datta, S., and Lorenz, D. (2020) <doi:10.1177/0962280220928572>, 
    Nevalainen, J., Oja, H., and Datta, S. (2017) <doi:10.1002/sim.7288>
    Dutta, S. and Datta, S. (2015) <doi:10.1111/biom.12447>, 
    Lorenz, D., Datta, S., and Harkema, S. (2011) <doi:10.1002/sim.4368>, 
    Datta, S. and Satten, G. (2008) <doi:10.1111/j.1541-0420.2007.00923.x>, 
    Datta, S. and Satten, G. (2005) <doi:10.1198/016214504000001583>.
	"""
	
	cran = "htestClust" 

	version("0.2.2", md5="58145baee43c5374fc9409ad5d8c08ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
