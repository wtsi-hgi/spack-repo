# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatopic(RPackage):
	"""Topic Inference to Identify Tissue Architecture in Multiplexed
Images

	A novel spatial topic model to integrate both cell type and spatial information to identify the complex spatial tissue architecture on multiplexed tissue images without human intervention. The Package implements a Collapsed Gibbs sampling algorithm for inference. 'SpaTopic' is scalable to large-scale image datasets without extracting neighborhood information for every single cell. For more details on the methodology, see <https://xiyupeng.github.io/SpaTopic/>.
	"""
	
	homepage = "https://github.com/xiyupeng/SpaTopic"
	cran = "SpaTopic" 

	version("1.0.1", md5="d7457b232cbbe7c200dc21c66df3e05d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rann@2.6:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-iterators@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
