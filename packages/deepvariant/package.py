import os
import shutil

from spack.package import *


class Deepvariant(Package):
    """DeepVariant is a deep learning-based variant caller for germline,
    somatic, long-read, RNA, and hybrid pipelines."""

    homepage = "https://github.com/google/deepvariant"
    url = "https://github.com/google/deepvariant/archive/refs/tags/v1.10.0.tar.gz"

    license("BSD-3-Clause")

    version("1.10.0", sha256="bee56524a4e6da69848c629f34fdb061623c8c3481762bc9ab7b0f05b1e0c537")

    resource(
        name="tensorflow",
        url="https://github.com/tensorflow/tensorflow/archive/refs/tags/v2.16.1.tar.gz",
        sha256="c729e56efc945c6df08efe5c9f5b8b89329c7c91b8f40ad2bb3e13900bd4876d",
        placement="tensorflow-src",
    )

    depends_on("bazel@6.5.0:", type="build")
    depends_on("python@3.10", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-tensorflow@2.16.1", type=("build", "run"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-protobuf@4:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-intervaltree", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-typing-extensions@4.10:", type=("build", "run"))
    depends_on("py-httplib2", type=("build", "run"))
    depends_on("py-google-auth", type=("build", "run"))
    depends_on("py-google-auth-httplib2", type=("build", "run"))
    depends_on("py-google-api-python-client", type=("build", "run"))
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-altair", type=("build", "run"))
    depends_on("py-ml-collections", type=("build", "run"))
    depends_on("py-etils", type=("build", "run"))
    depends_on("py-ml-dtypes@0.5.4:", type=("build", "run"))
    depends_on("py-pyparsing@3:", type=("build", "run"))
    depends_on("parallel", type="run")
    depends_on("zip", type="build")
    depends_on("unzip", type="build")
    depends_on("zlib-api")

    def _python_site_packages(self):
        python = self.spec["python"].command
        output = python(
            "-c",
            "import sysconfig; print(sysconfig.get_path('platlib'))",
            output=str,
        )
        return output.strip()

    def _prepare_tensorflow_repo(self):
        tf_src = join_path(self.stage.source_path, "tensorflow-src")
        tf_dest = join_path(self.stage.source_path, "..", "tensorflow")
        mkdirp(os.path.dirname(tf_dest))
        if os.path.islink(tf_dest) or os.path.isfile(tf_dest):
            os.remove(tf_dest)
        elif os.path.isdir(tf_dest):
            shutil.rmtree(tf_dest)
        os.symlink(tf_src, tf_dest)

    def install(self, spec, prefix):
        python_exe = spec["python"].command.path
        site_packages = self._python_site_packages()

        env = os.environ.copy()
        env["PYTHON_BIN_PATH"] = python_exe
        env["PYTHON_LIB_PATH"] = site_packages
        env.setdefault("PYTHONHOME", str(spec["python"].prefix))
        env["DV_USE_PREINSTALLED_TF"] = "1"
        env["DV_GPU_BUILD"] = "0"
        env["TF_NEED_GCP"] = "1"
        env["PYTHONPATH"] = ":".join(
            filter(None, [site_packages, env.get("PYTHONPATH")])
        )
        env["HOME"] = self.stage.path

        self._prepare_tensorflow_repo()

        bash = which("bash")
        with working_dir(self.stage.source_path):
            bash("build_release_binaries.sh", env=env)

            mkdirp(prefix.bin)
            binaries = [
                "deepvariant/train",
                "deepvariant/call_variants",
                "deepvariant/load_gbz_into_shared_memory",
                "deepvariant/make_examples",
                "deepvariant/make_examples_pangenome_aware_dv",
                "deepvariant/make_examples_somatic",
                "deeptrio/make_examples",
                "deepvariant/postprocess_variants",
                "deepvariant/vcf_stats_report",
                "deepvariant/show_examples",
                "deepvariant/runtime_by_region_vis",
                "deepvariant/convert_to_saved_model",
                "deepvariant/multisample_make_examples",
                "deepvariant/labeler/labeled_examples_to_vcf",
            ]
            for rel_path in binaries:
                exe_path = join_path("bazel-out", "k8-opt", "bin", rel_path)
                if not os.path.exists(exe_path):
                    continue
                install(exe_path, prefix.bin)
                zip_path = exe_path + ".zip"
                if os.path.exists(zip_path):
                    install(zip_path, prefix.bin)

            shared_obj = join_path(
                self.stage.source_path, "deepvariant", "examples_from_stream.so"
            )
            if os.path.exists(shared_obj):
                mkdirp(prefix.lib)
                install(shared_obj, prefix.lib)

    @run_after("install")
    def install_test(self):
        exe_path = join_path(self.prefix.bin, "make_examples")
        if not os.path.exists(exe_path):
            return
        with working_dir("spack-test", create=True):
            Executable(exe_path)("--help")
