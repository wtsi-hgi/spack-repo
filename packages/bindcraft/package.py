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
#     spack install bindcraft
#
# You can edit this file again by typing:
#
#     spack edit bindcraft
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Bindcraft(Package):
    """BindCraft is a user-friendly and accurate binder design pipeline using AlphaFold2 backpropagation, MPNN, and PyRosetta."""

    homepage = "https://github.com/martinpacesa/BindCraft"
    url = "https://github.com/martinpacesa/BindCraft/archive/refs/tags/v1.5.1.tar.gz"

    maintainers("martinpacesa")

    license("MIT")

    version("1.5.1", sha256="d4ddc3d8bee9a6ec28713aa95ee7f38499ab0091afed41c890b72b7a1e401b55")

    # Python dependencies
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pip", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy@:1.99.99", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pdbfixer", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-jupyter", type=("build", "run"))
    depends_on("py-fsspec", type=("build", "run"))
    depends_on("py-py3dmol", type=("build", "run"))
    depends_on("py-chex", type=("build", "run"))
    depends_on("py-dm-haiku", type=("build", "run"))
    depends_on("py-flax@:0.9.99", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-ml-collections", type=("build", "run"))
    depends_on("py-immutabledict", type=("build", "run"))
    depends_on("py-optax", type=("build", "run"))
    depends_on("py-jaxlib", type=("build", "run"))
    depends_on("py-jax", type=("build", "run"))
    depends_on("py-colabdesign", type=("build", "run"))
    # System dependencies
    depends_on("ffmpeg", type=("build", "run"))
    # depends_on("pyrosetta", type=("build", "run"))
    depends_on("cuda", type=("build", "run"))
    depends_on("cudnn", type=("build", "run"))
    depends_on("wget", type=("build", "run"))

    def install(self, spec, prefix):
        # Create params directory and download AlphaFold2 weights
        params_dir = join_path(prefix, "params")
        mkdirp(params_dir)

        # Download AlphaFold2 weights
        wget = which("wget")
        wget(
            "-O",
            join_path(params_dir, "alphafold_params_2022-12-06.tar"),
            "https://storage.googleapis.com/alphafold/alphafold_params_2022-12-06.tar",
        )

        # Extract weights
        tar = which("tar")
        tar("-xf", join_path(params_dir, "alphafold_params_2022-12-06.tar"), "-C", params_dir)

        # Remove archive
        remove(join_path(params_dir, "alphafold_params_2022-12-06.tar"))

        # Install main package files
        install_tree(".", prefix)

        # Make executables
        chmod = which("chmod")
        chmod("+x", join_path(prefix, "functions/dssp"))
        chmod("+x", join_path(prefix, "functions/DAlphaBall.gcc"))

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.prepend_path("PYTHONPATH", self.prefix)
