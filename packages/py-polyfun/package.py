# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from os import chmod

class PyPolyfun(Package):
    """ PolyFun estimates prior causal probabilities for SNPs, which can then be used by fine-mapping methods like SuSiE or FINEMAP. Unlike previous methods for functionally-informed fine-mapping, PolyFun can aggregate polygenic data from across the entire genome and hundreds of functional annotations. """

    homepage = "https://github.com/omerwe/polyfun"
    git = "https://github.com/omerwe/polyfun.git"

    version("2024-03-05", commit="0a6a863acccbec9ca4e4f4bdd72e44ff97dd4033")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pandas@0.25.0:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-bitarray", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-pandas-plink", type=("build", "run"))
    depends_on("py-rpy2", type=("build", "run"))
    depends_on("py-deprecated", type=("build", "run"))
    depends_on("py-fastparquet", type=("build", "run"))
    depends_on("py-imagecodecs", type=("build", "run"))
    depends_on("r-susier", type=("build", "run"))
    depends_on("r-ckmeans-1d-dp", type=("build", "run"))
    depends_on("finemap", type=("build", "run"))

    def patch(self):
        filter_file("parser.add_argument('--finemap-exe', default=None", "parser.add_argument('--finemap-exe', default='"+ self.spec["finemap"].prefix.bin + "/finemap_v1.4.2_x86_64" + "'", "test_polyfun.py", string=True)
        filter_file("parser.add_argument('--finemap-exe', default=None", "parser.add_argument('--finemap-exe', default='"+ self.spec["finemap"].prefix.bin + "/finemap_v1.4.2_x86_64" + "'", "finemapper.py", string=True)
        filter_file("parser.add_argument('--method'", "parser.add_argument('--method', default='finemap'", "finemapper.py", string=True)
        filter_file("susie_suff_stat", "susie_rss", "finemapper.py", string=True)

    def install(self, spec, prefix):
        cd("..")
        mkdir(prefix.opt)
        mkdir(prefix.bin)
        install_tree("spack-src", prefix.opt.polyfun)

        for py in ["aggregate_finemapper_results.py", "compute_ldscores.py", "compute_ldscores_from_ld.py", "create_finemapper_jobs.py", "extract_annotations.py", "extract_snpvar.py", "finemapper.py", "ldsc.py", "munge_polyfun_sumstats.py", "polyfun.py", "polyfun_utils.py", "polyloc.py", "polypred.py", "test_polyfun.py"]:
            exe = prefix.bin + "/" + py
            with open(exe, "w") as f:
                f.write("#!/bin/bash\nPYTHONPATH=\"$PYTHONPATH:"+prefix+"/opt/polyfun\" python3 "+prefix+"/opt/polyfun/"+py+" \"$@\"")
            chmod(exe, 0o755)
