# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Knowledgebase(Package):
    """Full-stack reference application that pairs a Next.js frontend with a
    FastAPI backend for serving large language model knowledge bases."""

    homepage = "https://github.com/wtsi-hgi/llm-knowledge-base"
    git = "https://github.com/wtsi-hgi/llm-knowledge-base.git"

    maintainers("vvi")

    license("MIT")

    version("20251209", commit="922fc02dbc99115889bd8313531cbf1b1f83bc27")

    depends_on("python@3.11:", type=("build", "run"))

    def install(self, spec, prefix):
        install_tree("backend", prefix.backend)
        install_tree("frontend", prefix.frontend)
        install("README.md", prefix)
        install("LICENSE", prefix)
        install("run-dev.sh", prefix)

    def setup_run_environment(self, env):
        env.set("KNOWLEDGEBASE_ROOT", self.prefix)
        env.set("KNOWLEDGEBASE_BACKEND", join_path(self.prefix, "backend"))
        env.set("KNOWLEDGEBASE_FRONTEND", join_path(self.prefix, "frontend"))

    @run_after("install")
    def install_test(self):
        python = self.spec["python"].command
        python(
            "-c",
            "import compileall, pathlib; compileall.compile_dir(str(pathlib.Path(r'{0}')), quiet=1)".format(
                join_path(self.prefix, "backend")
            ),
        )
