require "logger"

# Jekyll 3.9.0, as bundled by this GitHub Pages theme, calls Logger#level before
# Ruby 3.3 has initialized Logger's fiber-local level override table.
class Logger
  unless method_defined?(:vercel_original_level_for_ruby33)
    alias_method :vercel_original_level_for_ruby33, :level
  end

  def level
    @level_override ||= {}
    vercel_original_level_for_ruby33
  end
end

load Gem.bin_path("jekyll", "jekyll")
