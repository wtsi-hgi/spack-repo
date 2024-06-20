# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install rasp-model
#
# You can edit this file again by typing:
#
#     spack edit rasp-model
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import os


class RaspModel(PythonPackage):
    """
    This repository contains scripts and data to repeat the analyses in Blaabjerg et al.:
    "Rapid protein stability prediction using deep learning representations".
    """

    homepage = "https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg"
    git = "https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg"

    license("Apache 2.0")

    version("main", branch="main")

    depends_on("py-pyyaml")
    depends_on("py-scikit-learn")
    depends_on("py-mpl-scatter-density")
    depends_on("py-pdbfixer")
    depends_on("py-torch")
    depends_on("py-vaex")
    depends_on("py-biopython@:1.73")
    depends_on("openmm")
    depends_on("py-seaborn")
    depends_on("py-ptitprince")
    depends_on("dssp")
    depends_on("reduce")

    patch("add_argparse_to_run_pipeline.patch")

    def patch(self):
        filter_file(
            "#!/usr/bin/python", "#!" + self.spec["python"].prefix.bin.python, "src/run_pipeline.py", string=True
        )
        filter_file(
            "dir=$(pwd)", "dir=$(dirname $(dirname $0))", "src/pdb_parser_scripts/parse_pdbs_pred.sh", string=True
        )
        filter_file(
            "reduce_exe=$dir/pdb_parser_scripts/reduce/reduce_src/reduce",
            f"reduce_exe={self.spec['reduce'].prefix.bin.reduce}",
            "src/pdb_parser_scripts/parse_pdbs_pred.sh",
            string=True,
        )

        with open("pyproject.toml", "w") as fh:
            fh.write(
                '[project]\nname = "RaSP-Model"\nversion = "1.0"\ndependencies = []\n[tool.setuptools.packages.find]\nwhere = ["src"]'
            )

    @run_after("install")
    def post(self):
        mkdir(self.prefix.bin)
        os.chmod("src/run_pipeline.py", 0o755)
        install_tree("src", self.prefix.bin)
