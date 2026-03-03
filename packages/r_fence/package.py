# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFence(RPackage):
	"""Using Fence Methods for Model Selection

	This method is a new class of model selection strategies, 
    for mixed model selection, which includes linear and generalized linear 
    mixed models. The idea involves a procedure to isolate a subgroup of what 
    are known as correct models (of which the optimal model is a member). This is 
    accomplished by constructing a statistical fence, or barrier, to carefully 
    eliminate incorrect models. Once the fence is constructed, the optimal model is 
    selected from among those within the fence according to a criterion which can 
    be made flexible.
    References: 
    1. Jiang J., Rao J.S., Gu Z., Nguyen T. (2008),  Fence Methods for Mixed Model Selection. 
    The Annals of Statistics, 36(4): 1669-1692.  
    <DOI:10.1214/07-AOS517> <https://projecteuclid.org/euclid.aos/1216237296>.
    2. Jiang J., Nguyen T., Rao J.S. (2009), A Simplified Adaptive Fence Procedure. 
    Statistics and Probability Letters, 79, 625-629.  
    <DOI:10.1016/j.spl.2008.10.014> <https://www.researchgate.net/publication/23991417_A_simplified_adaptive_fence_procedure>
    3. Jiang J., Nguyen T., Rao J.S. (2010), Fence Method for Nonparametric Small Area Estimation. 
    Survey Methodology, 36(1), 3-11.  
    <http://publications.gc.ca/collections/collection_2010/statcan/12-001-X/12-001-x2010001-eng.pdf>.
    4. Jiming Jiang, Thuan Nguyen and J. Sunil Rao (2011), Invisible fence methods and the identification of differentially expressed gene sets. 
    Statistics and Its Interface, Volume 4, 403-415.
    <http://www.intlpress.com/site/pub/files/_fulltext/journals/sii/2011/0004/0003/SII-2011-0004-0003-a014.pdf>.
    5. Thuan Nguyen & Jiming Jiang (2012), Restricted fence method for covariate selection in longitudinal data analysis. 
    Biostatistics, 13(2), 303-314.  
    <DOI:10.1093/biostatistics/kxr046> <https://academic.oup.com/biostatistics/article/13/2/303/263903/Restricted-fence-method-for-covariate-selection-in>.
    6. Thuan Nguyen, Jie Peng, Jiming Jiang (2014), Fence Methods for Backcross Experiments.  
    Statistical Computation and Simulation, 84(3), 644-662.  
    <DOI:10.1080/00949655.2012.721885> <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3891925/>.
    7. Jiang, J. (2014), The fence methods, in Advances in Statistics, Hindawi Publishing Corp., Cairo.  
    <DOI:10.1155/2014/830821>.
    8. Jiming Jiang and Thuan Nguyen (2015), The Fence Methods, World Scientific, Singapore.  
    <https://www.abebooks.com/9789814596060/Fence-Methods-Jiming-Jiang-981459606X/plp>.
	"""
	
	cran = "fence" 

	version("1.0", md5="f851e6da48150495d7d2e1a3953d8f5b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sae", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
