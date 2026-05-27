# Copyright 2013-2025 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfbs(Package):
    """Transcription factor motif and binding site resources released by the
    Taipale Lab. The repository bundles curated motif collections, example R
    projects, and helper scripts for reproducing the analyses from Xie et al.
    2025."""

    homepage = "https://github.com/MariaOsmala/TFBS"
    url = "https://github.com/MariaOsmala/TFBS/archive/refs/tags/v1.0.0.tar.gz"

    license("MIT", "LICENSE.txt")

    version("1.0.0", sha256="d748376f36016ed8a14d1be2560a40b7de794a2e3ef64467e5e124ad9aa1bb30")

    depends_on("r@4.2:", type="run")

    def install(self, spec, prefix):
        tfbs_dir = join_path(prefix.share, "tfbs")
        install_tree(".", tfbs_dir)

    @run_after("install")
    def install_test(self):
        tfbs_dir = join_path(self.prefix.share, "tfbs")
        python3 = which("python3")
        python3(
            "-c",
            (
                'import pathlib; d = pathlib.Path(r"{0}"); '
                'readme = d / "README.md"; '
                'assert d.is_dir() and readme.is_file(), "TFBS data not installed correctly"'
            ).format(tfbs_dir),
        )
