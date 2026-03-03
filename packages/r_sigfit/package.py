from spack.package import *


class RSigfit(RPackage):
    """Flexible Bayesian inference of mutational signatures.

    Implements Bayesian models for fitting and extracting mixtures of
    mutational signatures from mutation count data, with interfaces to
    multinomial, Poisson, normal, and negative binomial models. MCMC
    sampling is performed using Stan.
    """

    homepage = "https://github.com/kgori/sigfit"
    url = "https://github.com/kgori/sigfit/archive/refs/tags/v2.2.0.tar.gz"

    version("2.2.0", sha256="c56f104b1da1cbe91380d008dd1f16df4ed275ed81893ded983a3506ca191aa7")

    license("GPL-3.0-or-later")

    depends_on("r@3.4.0:", type=("build", "run"))

    # Imports
    with default_args(type=("build", "run")):
        depends_on("r-rcpp@0.12.0:")
        depends_on("r-rstan@2.18.1:")
        depends_on("r-rstantools@2.0.0:")
        depends_on("r-coda@0.19:")
        depends_on("r-clue@0.3:")
        depends_on("r-knitr")
        depends_on("r-rmarkdown")
        # LinkingTo
        depends_on("r-bh@1.66.0:")
        depends_on("r-rcppeigen@0.3.3.3.0:")
        depends_on("r-stanheaders@2.18.0:")
        # Suggests
        depends_on("r-markdown")

